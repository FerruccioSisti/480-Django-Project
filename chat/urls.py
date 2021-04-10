# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mainpage/', views.mainpage, name='mainpage'),
    path('<str:room_name>/', views.room, name='room'),
]