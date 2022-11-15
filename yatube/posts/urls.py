# post/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    path('index.html', views.index),
    path('group_list.html', views.group_list),
    path('group/<slug:slug>/', views.group_posts)
]