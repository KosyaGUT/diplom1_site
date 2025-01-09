from django.shortcuts import render
from news.models import News

# Функция для получения только опубликованных новостей
def get_published_news():
  return News.objects.filter(is_published=False).order_by('-published_date')

# Представление для отображения списка новостей
def news_index(request):
  news_items = get_published_news()

  context = {
    'title': 'Новости',
    'news': news_items,
  }

  return render(request, 'home/news.html', context)
