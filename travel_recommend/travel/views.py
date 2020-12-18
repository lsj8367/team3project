from django.shortcuts import render
from django.http.response import HttpResponse
from travel.utils import get_db_handle, get_collection_handle
import json
import random
from django.views.decorators.csrf import csrf_exempt # csrf 보호 ajax post

db_handle, mongo_client = get_db_handle('testdb', 'localhost', '27017')

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

@csrf_exempt
def SearchFunction(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        #search = request.GET.get('search')
        #print(search)
        
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        if start_date == '':
            start_date = None
        if end_date == '':
            end_date = None
        
#         print(search)
#         print(start_date)
#         print(end_date)
        
        collection_handle = get_collection_handle(db_handle, 'testdb')
        #data = collection_handle.find({'도시' : '충주'}) # 도시가 충주인것 찾음
        try:
            data = collection_handle.find_one({'도시' : search}) # 한개만 찾을때
            print(data['도시']) # 부산광역시
            print(data)
            #list1 = {} # 루트1
    #        list2 = {} # 루트2
    #        list3 = {} # 루트3
    #        list4 = {} # 루트4
    #        list5 = {} # 루트5
            print()
            
            # 루트 5개만 하고 멈춤
        #         for i in range(0, 25, 5):
        #             print(data['장소'][i : i + 5])
        #             print(data['주소'][i : i + 5])
        #             print()
            globals()['list1'] = []
            globals()['list2'] = []
            globals()['list3'] = []
            globals()['list4'] = []
            globals()['list5'] = []
            try:
                for i in range(5):
                    #print(random.sample(data['장소'], 5))
                    #print(random.sample(data['주소'], 5))
                    globals()['list{}'.format(i + 1)] = {'장소' : random.sample(data['장소'], 5), "주소" : random.sample(data['주소'], 5)}
                print(globals()['list1'])
                print(globals()['list2'])
                print(globals()['list3'])
                print(globals()['list4'])
                print(globals()['list5'])
                
            except:
                print("globals 에러")
                list1 = {'장소' : random.sample(data['장소'], len(data['장소'])), '주소' : random.sample(data['주소'], len(data['주소']))}
                print(list1)
            
            
            weather = 'rainy'
            # root = ['루트1', '루트2', '루트3', '루트4', '루트5']
            list = []
            
            if not len(globals()['list1']) == 0:
                root = {
                    '루트1' : globals()['list1'],
                    '루트2' : globals()['list2'],
                    '루트3' : globals()['list3'],
                    '루트4' : globals()['list4'],
                    '루트5' : globals()['list5'],
                        }
                print(root)
                tour = random.sample(data['장소'], len(data['장소']))
            
            else:
                print('5개 이하임')
                root = {
                        '루트1' : list1
                    }
                tour = random.sample(data['장소'], len(data['장소']))            
                print(root)
            # tour = ['여행지1', '여행지2', '여행지3', '여행지4', '여행지5']
            
            restaurant = ['음식점1', '음식점2', '음식점3', '음식점4', '음식점5']
            list.append(root)
            
            #context={'travel':search, 'start':start_date, 'end':end_date, 'root':root, 'tour':tour, 'restaurant':restaurant}
            #return render(request, 'main.html', json.dumps(list))
            return HttpResponse(json.dumps(list), content_type = 'application/json')
        except:
            list = []
            print('도시 없음')
            return HttpResponse(json.dumps(list), content_type = 'application/json') # null값을 줘버림
    
def DetailFunction(request):
    return render(request, 'detail.html')