from django.urls import path

from news.views import *

from django.conf import settings
from django.conf.urls.static import static

app_name = 'news'

urlpatterns = [
    path('news/', news_index, name='news'),
    path('news/<int:news_id>/', news_detail, name='news_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)