from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from travel.utils import get_db_handle, get_collection_handle

db_handle, mongo_client = get_db_handle('testdb', 'localhost', '27017')
# testdb 는 데이터베이스명 주소 localhost 자기주소 27017이 기본 포트번호

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def SearchFunction(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        if start_date == '':
            start_date = None
        if end_date == '':
            end_date = None
        
        print(search)
        print(start_date)
        print(end_date)
        
        conn = get_collection_handle(db_handle, 'testdb') # 여기서 test_db는 collections이므로 table과 같음.
        # 사용하려면  conn.find or insert delete update 가능
        
        #data = conn.find({'도시' : '충주'}) # 도시가 충주인것 찾음
        data = conn.find_one() # 한개만 찾을때
        print(data)
        
        weather = 'rainy'
        root = ['루트1', '루트2', '루트3', '루트4', '루트5']
        tour = ['여행지1', '여행지2', '여행지3', '여행지4', '여행지5']
        restaurant = ['음식점1', '음식점2', '음식점3', '음식점4', '음식점5']
        
        
        context={'travel':search, 'start':start_date, 'end':end_date, 'root':root, 'tour':tour, 'restaurant':restaurant}
        return render(request, 'main.html', context)
    
def DetailFunction(request):
    
    return render(request, 'datail.html')