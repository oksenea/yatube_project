from django.shortcuts import render
from django.http import HttpResponse
# Импортируем загрузчик.
from django.template import loader


def index(request):
    # Загружаем шаблон;
    # шаблоны обычно хранят в отдельной директории.
    template = 'posts/index.html'
    # Формируем шаблон
    return render(request, template)


def group_list(request):
    # Загружаем шаблон;
    # шаблоны обычно хранят в отдельной директории.
    template = 'posts/group_list.html'
    # Формируем шаблон
    return render(request, template)


def group_posts(reqest, slug):
    # Загружаем шаблон;
    # шаблоны обычно хранят в отдельной директории.
    template = f'posts/group-{slug}.html'
    # Формируем шаблон
    return render(request, template) 
