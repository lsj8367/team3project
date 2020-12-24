from django.contrib import admin
from django.urls import path
from recommend_app import views
import recommend_app
from recommend_app import cal_knn

urlpatterns = [
    path('result_knn', recommend_app.views.Cal_Knn),
    path('result_svd', recommend_app.views.Cal_Svd),
    ]