from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('create_user', views.create_user), 
    path('user_login', views.user_login),
    path('logout', views.logout)
]
