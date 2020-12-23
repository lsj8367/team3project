from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from travel.models import Travel, Tuser, Treview
# from travel.utils import get_db_handle, get_collection_handle
from travel.weather import Weather

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

def MainFunc(request):
    user_log = request.session.get('user')
    print(user_log) # 세션 값 = 사용자 이름
    
    return render(request, 'main.html', {'user_log' : user_log})

def SearchFunction(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        user_log = request.session.get('user')
        print(user_log) # 세션 값 = 사용자 이름
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
        
        travel = Travel.objects.all()
        tuser = Tuser.objects.all()
        treview = Treview.objects.all()
        

        root = ['루트1', '루트2', '루트3', '루트4', '루트5']
        tour = ['여행지1', '여행지2', '여행지3', '여행지4', '여행지5']
        
        context={'travel':search, 'start':start_date, 'end':end_date, 'weather': wlist, 'root':root, 'tour':tour, \
                  'user_log' : user_log}
        return render(request, 'main.html', context)
    
    
def DetailFunction(request):
    return render(request, 'detail2.html')

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
        
        print(name, ID, password)
        print(travel1, travel2, travel3)
        print(rating1, rating2, rating3)
        
        return redirect('home')
    return render(request, 'datail.html')

