from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('room/', views.room, name='room'),
    path('room/chat/<str:room_name>/', views.chat, name='chat_room'),
]