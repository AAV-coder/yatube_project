from django.urls import path, include
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Список постов
    path('posts/', views.group_posts),
    # Подробная информация о групповом посте. Ждем переменную типа int,
    # и будем использовать ее под именем pk
    path(
        'posts/<int:pk>/',
        views.group_posts_detail
    ),
] 