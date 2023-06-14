from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def listings(request):
    return render(request, 'pages/index.html')


def register(request):
    return render(request, 'pages/index.html')


def login(request):
    return render(request, 'pages/index.html')
