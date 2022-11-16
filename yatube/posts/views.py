from django.shortcuts import render
from django.http import HttpResponse
# Импортируем загрузчик.
from django.template import loader


def index(request):
    # Загружаем шаблон;
    # шаблоны обычно хранят в отдельной директории.
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
    }
    # Формируем шаблон
    return render(request, template, context)


def group_list(request):
    template = 'posts/group_list.html'
    title = 'Группа тайных поклонников графа.'
    context = {
        'title': title,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_posts.html'
    title = f'Группа-{slug}'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'text': text,
        'title': title,
    }
    return render(request, template, context)
