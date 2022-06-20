from django.urls import path
from . import views

urlpatterns = [
    # Страница групповых постов
    path('group/<slug:slug>', views.group_posts),    
    # Главная страница
    path('', views.index),
] 