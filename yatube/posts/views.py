from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(reqest):
    return HttpResponse('Main')

def group_posts(reqest, slug):
    return HttpResponse(f'String: {slug}')
