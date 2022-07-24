from django.urls import path

from . import views

urlpatterns = [

    path('', views.home),
    path('contact/<str:name>', views.contact),
    path('home/', views.myhome),
    path('join/', views.join, name='join'),


]
