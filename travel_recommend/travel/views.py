from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.urls import reverse

from travel.models import Travel, Tuser, Treview
# from travel.utils import get_db_handle, get_collection_handle

########### 수정
import MySQLdb
from django.db.models import Max
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
##################


def IndexFunc(request):
    return render(request, 'index.html')

def LoginFunc(request):
    id = request.POST.get('id')
    pwd = request.POST.get('pwd')
    #print(id)
    #print(pwd)

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
        print(user.user_pwd)
        if user.user_pwd != pwd:
            return render(request, 'index.html')
        
        request.session['user'] = user.user_name
        return redirect('main') # urls에 name값 할당
        
def LogoutFunc(request):
    print(request.session.get('user'))
    if request.session.get('user'):
        del(request.session['user'])
    #print(request.session.get('user')) # 세션 삭제된것 확인
    return redirect('home')


# Create your views here.
def MainFunc(request):
    user_log = request.session.get('user')
    print(user_log) # 세션 값 = 사용자 이름
    
    
    return render(request, 'main.html', {'user_log' : user_log})

def SearchFunction(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        weather = 'rainy'

        if start_date == '':
            start_date = None
            weather = ''
        if end_date == '':
            end_date = None
            weather = ''    
        
        print(search)
        print(start_date)
        print(end_date)
        

        ###
        ### 데이터 분석 받아오는곳
        ###
        
        travel = Travel.objects.all()
        tuser = Tuser.objects.all()
        treview = Treview.objects.all()  
        
        weather = 'rainy'

        root = ['루트1', '루트2', '루트3', '루트4', '루트5']
        tour = ['여행지1', '여행지2', '여행지3', '여행지4', '여행지5']
        restaurant = ['음식점1', '음식점2', '음식점3', '음식점4', '음식점5']
        
        
        context={'travel':search, 'start':start_date, 'end':end_date, 'weather':weather, 'root':root, 'tour':tour, 'restaurant':restaurant}
        #return render(request, 'main.html', context)
        return render(request, 'main.html', context)
        return HttpResponseRedirect(reverse(''))
    
    
def DetailFunction(request):
    return render(request, 'detail2.html')

def SignupFunction(request):
    
    return render(request, 'signup.html')

######## 수정 
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
#             sql = "insert into tuser values('{}', '{}', '{}')".format(ID, name, password)
#             cursor = conn.cursor()
#             cursor.execute(sql)
#             conn.commit()
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
        

    return render(request, 'main.html')

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
######## 수정 