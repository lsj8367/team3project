from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect

from django.urls import reverse

from travel.models import Travel, Tuser, Treview
# from travel.utils import get_db_handle, get_collection_handle
 
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
        #return render(request, 'main.html', context)
        return HttpResponseRedirect(reverse('main'))
    
    
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

