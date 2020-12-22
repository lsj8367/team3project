from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

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
        
        return render(request, 'main.html')