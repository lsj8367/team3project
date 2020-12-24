from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from travel.models import Travel, Tuser, Treview
import MySQLdb
from django.db.models import Max
from travel.weather import Weather
from travel.cosine_sim import cosinePlace
import json
import numpy as np
import recommend_app
from recommend_app.cal_knn import results
import os

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}
conn = MySQLdb.connect(**config)

# Create your views here.

def IndexFunc(request):
    return render(request, 'index.html')

def LoginFunc(request):
    id = request.POST.get('id')
    pwd = request.POST.get('pwd')

    if Tuser.objects.filter(user_id = id).exists() == True:
        tusers = Tuser.objects.filter(user_id = id)
    else:
        ss = '''
            <script> 
                alert('아이디 또는 비밀번호가 일치하지 않습니다');
                history.back();
            </script>
        '''
        return render(request, 'index.html', {'error' : ss})
    
    for user in tusers:
        #print(user.user_pwd)
        if user.user_pwd != pwd:
            return render(request, 'index.html')
        
        request.session['user'] = user.user_name
        return redirect('main') # urls에 name값 할당
        
def LogoutFunc(request):
    #print(request.session.get('user'))
    if request.session.get('user'):
        del(request.session['user'])
    #print(request.session.get('user')) # 세션 삭제된것 확인
    return redirect('home')

def MainFunc(request):
    user_log = request.session.get('user')
    #print(user_log) # 세션 값 = 사용자 이름
    
    return render(request, 'main.html', {'user_log' : user_log})

def SearchFunction(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        user_log = request.session.get('user')
        
        #print(user_log) # 세션 값 = 사용자 이름
        #print(search)

        if start_date == '':
            start_date = None
            weather = ''
        if end_date == '':
            end_date = None
            weather = ''
            
        wlist = []
        # 날씨 출력    
        try:
            weather = Weather(search)
            
            query = (weather['date'] >= start_date) & (weather['date'] <= end_date)
            
            for i in range(len(weather.loc[query]['weather'].values)):
                
                w = weather.loc[query]['weather'].values[i]
                if (w >= 1 and w <= 3) or (w >= 33 and w <= 35):
                    w = '맑음'
                elif (w >= 4 and w <= 5) or (w >= 36 and w <= 37):
                    w = '구름 조금'
                elif (w >= 6 and w <= 8) or (w == 38):
                    w = '흐림'
                elif (w == 11):
                    w = '안개'
                elif (w == 12 or w == 13):
                    w = '소나기'
                elif (w >= 14 and w <= 17) or (w == 39):
                    if (w == 15 or w == 16) or (w == 41 or w == 42):
                        w = '천둥번개와 비'
                    w = '한때 비'
                elif w == 18 and w <= 40:
                    if (w >= 19 and w <= 21) or (w == 32):
                        w = '강풍'
                    elif(w == 23 or w == 24) or (w == 29) or (w == 43 or w == 44):
                        w = '눈'
                    elif(w == 25):
                        w = '진눈깨비'
                    elif(w == 26):
                        w = '얼어붙은 비'
                    w = '비'
                elif w == 30:
                    w = '뜨거움 - 주의'
                elif w == 31:
                    w = '추움 - 주의'
                wlist.append(w)
            print(wlist)   
        except: 
            print('===날짜가 없을경우===')
            print(start_date)
            print(end_date)

        ###
        ### 데이터 분석 받아오는곳
        ###
        tuser = Tuser.objects.filter(user_name = user_log)
        for t in tuser:
            userid = t.user_id
        
        path = os.getcwd()
        print(path)
        
        filepath = path + '/travel_recommend/travel/static/datafile/placerating.csv'
        recommend_app.cal_knn.Cal_Knn(filepath, userid)
        print(results[0]['iid'].values) # 리스트 추천여행지 확인
        
        travel = Travel.objects.all()
        treview = Treview.objects.all()
        
        

        tour = ['여행지1', '여행지2', '여행지3', '여행지4', '여행지5']
        
        context={'travel':search, 'start':start_date, 'end':end_date, 'weather': wlist, 'tour':travel, 'user_log' : user_log}
        return render(request, 'main.html', context)

def CossimFunc(request):
    msg = request.GET['msg']
    way = request.GET['way']
    print(msg)
    df = cosinePlace(msg,way)
    print(len(df), df.iloc[0].title)
    datas = []
    for s in range(len(df)):
        dic = {'title':df.iloc[s].title, 'area':df.iloc[s].area, 'genre':df.iloc[s].genre, 'weighted_vote':np.round(df.iloc[s].weighted_vote,3)}
        datas.append(dic)
    return HttpResponse(json.dumps(datas), content_type = "application/json")
    
###### 수정 20201224
def DetailFunction(request):

    travel_id = request.GET.get('travel_id')
    travel = Travel.objects.get(tourid = travel_id)
    
    travels =  Travel.objects.filter(city = travel.city)|Travel.objects.filter(town = travel.town)
    # select * from travel where city = ? or town =? limit 5;
    travels = travels[:5]
    
    return render(request, 'detail2.html', {'travel':travel, 'travels':travels})


def SignupFunction(request):
    return render(request, 'signup.html')


def SignupFunction2(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        ID = request.POST.get('ID')
        password = request.POST.get('password')
        
        travel1 = request.POST.get('travel1')
        rating1 = request.POST.get('rating1')
        travel2 = request.POST.get('travel2')
        rating2 = request.POST.get('rating2')        
        travel3 = request.POST.get('travel3')
        rating3 = request.POST.get('rating3')        
        
        

        #유저등록
        if Tuser.objects.filter(user_id = ID).exists() == False:
            Tuser(
                user_id = ID,
                user_name = name,
                user_pwd = password
            ).save()

        else:
            ss = """
            <script> 
                alert('이미 존재하는 아이디입니다.');
                history.back();
            </script>
            """
            return render(request, 'signup.html', {'error' : ss})
             
        #리뷰등록
        try:
            
            InsertReview(ID, travel1, rating1)
            InsertReview(ID, travel2, rating2)
            InsertReview(ID, travel3, rating3)
        except:
            ss = '''
            <script> 
                alert('존재하는 여행지를 입력해주세요.');
                history.back();
            </script>
            '''
            return render(request, 'signup.html', {'error' : ss})
        

    return redirect('home')

def InsertReview(ID, travel, rating):
    obj = Treview.objects.aggregate(treview_no=Max('treview_no'))
    no = obj['treview_no'] + 1
    if no is None:
        no = 1
    
    try :
        obj = Travel.objects.get(city = travel)
    except:
        obj = Travel.objects.get(town = travel)
    travel = obj.tourid
    obj = Tuser.objects.get(user_id = ID)
    
    
    sql = "insert into treview values({}, '{}', {}, '{}')".format(no, ID, travel, rating)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
