from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.urls import reverse

from authentication.models import User
from authentication.forms import UserLoginForm

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
  if request.method == 'POST':
    form = UserLoginForm(data= request.POST)
    if form.is_valid():
      email = request.POST['email']
      password = request.POST['password']
      user = auth.authenticate(email=email, password=password)
      if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('publication_feed'))
  else:
    form = UserLoginForm()

  context = {
    'title': 'Вход',
    'form': form
  }

  return render(request, 'authentication/log.html', context)