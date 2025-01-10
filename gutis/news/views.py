from django.shortcuts import render
from news.models import News
from django.shortcuts import render, get_object_or_404

# Функция для получения только опубликованных новостей
def get_published_news():
  return News.objects.filter(is_published=True).order_by('-published_date')

# Представление для отображения списка новостей
def news_index(request):
  news_items = get_published_news()

  context = {
    'title': 'Новости',
    'news': news_items,
  }

  return render(request, 'home/news.html', context)

def news_detail(request, news_id):
  news_id_item = News.objects.get(news_id=news_id)
  news_view = get_object_or_404(News, news_id=news_id)
  news_view.views += 1  # Увеличиваем счетчик просмотров
  news_view.save()


  context = {
    "news": news_id_item,
    "news_view": news_view
  }
  return render(request, 'home/news_id.html', context)
