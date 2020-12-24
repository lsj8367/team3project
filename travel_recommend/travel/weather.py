import os
import pandas as pd

def Weather(cityname):
    path = os.getcwd()
    print(path)
    
    files=os.listdir(path + '/travel_recommend/travel/static/weather')
#     filename = path + '/weather'
    filename = path + '/travel_recommend/travel/static/weather'
    #print(files)
    
    for f in files:
        if f.startswith(cityname):
            weather = pd.read_excel(filename + '/' + f, index_col=0)
            #print(f)
    #print(weather)
    weather['date'] = pd.to_datetime(weather['date'])
    print(weather['date'])
    
    return weather

# a = pd.read_excel(path + '\project_weather\부산광역시.xlsx')
# print(a)


