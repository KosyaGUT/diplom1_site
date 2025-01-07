from django.shortcuts import render

def index(request):
  context = {
    'title': 'Лента публикаций',
  }

  return render(request, 'home/home.html', context)


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