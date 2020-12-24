"""travel_recommend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from travel import views
import recommend_app
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.IndexFunc, name='home'),
    path('login', views.LoginFunc),
    path('logout', views.LogoutFunc),
    path('main', views.MainFunc, name='main'), 
    path('search', views.SearchFunction),
    path('detail', views.DetailFunction),
    path('signup', views.SignupFunction),
    path('signup2', views.SignupFunction2),
<<<<<<< HEAD
    path('cal_svd',  include('recommend_app.urls')),
    path('cal_knn', include('recommend_app.urls')),
=======
    path('startajax', views.CossimFunc),
>>>>>>> branch 'main' of https://github.com/KICteam3Project/team3project.git
]
