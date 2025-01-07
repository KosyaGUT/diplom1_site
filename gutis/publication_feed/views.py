from django.shortcuts import render

def index(request):
  context = {
    'title': 'Лента публикаций',
  }

  return render(request, 'home/home.html', context)
