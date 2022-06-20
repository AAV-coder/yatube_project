from django.shortcuts import render

from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница!')


# Страница с групповыми постами
def group_posts(request):
    return HttpResponse('Групповые посты')