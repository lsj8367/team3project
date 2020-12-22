from django.shortcuts import render

# Create your views here.
import pandas as pd # raw dataset

# CNN
import numpy as np
import matplotlib.pyplot as plt

from keras.datasets import imdb
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# 1. raw dataset
num_features = 3000
sequence_length = 2000
embedding_dimension = 1000

rating = pd.read_csv("C:\work\Data_teampro\internal/placerating.csv")
rating.head()   #   critic(user)   title(item)   rating

# x, y 정의
x = rating['userId']
y = rating['rating']

print(len(x))
print(len(y))
"""
######## 스케일링 안하면 loss가 매우매우 작게 나옴 (음수...엄청난 자릿수로)

def vectorize_sequences(sequences, dimension=10000):
    # 크기가 (len(sequences), dimension)이고 모든 원소가 0인 행렬을 만듭니다.
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1. # results[i]에서 특정 인덱스의 위치를 1로 만듭니다.
    return results

x_train = vectorize_sequences(train_data) # 훈련 데이터를 벡터로 변환합니다.
x_test = vectorize_sequences(test_data) # 테스트 데이터를 벡터로 변환합니다.


# label 원 핫 인코딩
onehot = OneHotEncoder(categories = 'auto')
# print(onehot)
y = onehot.fit_transform(y[:,np.newaxis]).toarray()
# print(y[:5], y.shape)

#train_labels = np.reshape(train_labels, (-1, NUM_CLASSES)) you're changing the shape to [10, 5].

"""
# # # feature 표준화
scaler = StandardScaler()
x = np.asarray(x).astype('float32').reshape((-1,1))
#y = np.asarray(y).astype('float32').reshape((-1,1))
x_scale = scaler.fit_transform(x)

# y_scale = scaler.fit_transform(y)

# train / test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state = 1)


##### 표준화 후 차원 맞는 지 확인 필요.
# 요기부분
x_trains = []
for i in x_train:
  x_trains.append(x_train)

x_tests = []
for i in x_test:
  x_tests.append(x_test)


x_train = [x_train]
x_test = [x_test]
print(type(x_train))

x_train = pad_sequences(x_trains, maxlen = sequence_length)
x_test = pad_sequences(x_tests, maxlen = sequence_length)


def vectorize_sequences(sequences, dimension=10000):
    # 크기가 (len(sequences), dimension)이고 모든 원소가 0인 행렬을 만듭니다.
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1. # results[i]에서 특정 인덱스의 위치를 1로 만듭니다.
    return results

x_train = vectorize_sequences(x_train) # 훈련 데이터를 벡터로 변환합니다.
x_test = vectorize_sequences(x_test) # 테스트 데이터를 벡터로 변환합니다.