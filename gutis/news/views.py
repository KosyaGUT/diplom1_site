from django.shortcuts import render

def index(request):
  context = {
    'title': 'Новости',
  }

  return render(request, 'home/news.html', context)
