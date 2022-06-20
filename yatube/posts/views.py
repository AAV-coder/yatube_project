from django.shortcuts import render

from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница!')


# Страница с групповыми постами
def group_posts(request):
    return HttpResponse('Список групповых постов')


# В урл мы ждем параметр, и нужно его прередать в функцию для использования
def group_posts_detail(request, pk):
    return HttpResponse(f'Пост номер {pk}')