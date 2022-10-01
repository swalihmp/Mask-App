from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('reg/', views.reg, name='reg'),
    path('addmask/', views.addmask, name='addmask'),
    path('newmask/', views.newmask, name='newmask'),
    path('base/', views.base, name='base'),
    path('base1/', views.base1, name='base1'),
    path('login/',views.login,name='login'),
    path('maskrequest/',views.maskrequest,name='maskrequest'),
    path('makerequest/',views.makerequest,name='makerequest'),
    path('showrequests/',views.showrequests,name='showrequests'),
    path('profile/',views.profile,name='profile'),
    path('myrequests/',views.myrequests,name='myrequests'),
    
]