from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  context = {
    'title': 'Главная страница',
  }

  return render(request, 'authentication/home.html', context)


def registration(request):
  context = {
    'title': 'Регистрация',
  }

  return render(request, 'authentication/reg.html', context)


def login(request):
  context = {
    'title': 'Вход',
  }

  return render(request, 'authentication/log.html', context)