"""pyaat URL Configuration

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
from . import views


urlpatterns = [

    path('', views.index),
    path('postsign/', views.postsign),
    path('logout/', views.logout, name="log"),
    path('signup/', views.signin, name="signup"),
    path('login/', views.index, name="login"),
    path('student/', views.home, name="home"),
    path('home/', views.basic, name="basic"),
    path('academics/', views.academics, name="academics"),
    path('sem1/', views.sem1, name="sem1"),
    path('sem2/', views.sem2, name="sem2"),
    path('sem3/', views.sem3, name="sem3"),
    path('sem4/', views.sem4, name="sem4"),
    path('sem5/', views.sem5, name="sem5"),
    path('sem6/', views.sem6, name="sem6"),
    path('register/', views.register, name="register"),
    path('personal/', views.personal, name="personal"),
    path('dsem1/', views.dsem1),
    path('dsem2/', views.dsem2),
    path('dsem3/', views.dsem3),
    path('dsem4/', views.dsem4),
    path('dsem5/', views.dsem5),
    path('dsem6/', views.dsem6),
    path('studentserach/', views.studentserach, name="studentserach"),
    path('studentdetails/', views.studentdetails, name="studentdetails"),
    path('studsrc/', views.studsrc, name="studsrc"),
    path('acasrc/', views.acasrc, name="acasrc"),
    path('display/', views.display, name="display"),





]

