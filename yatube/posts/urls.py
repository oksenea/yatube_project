# post/urls.py
from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    # Главная страница
    path('', views.index),
    path('index.html', views.index, name='main'),
    path('group/<slug:slug>/', views.group_posts, name='group_posts')
]
