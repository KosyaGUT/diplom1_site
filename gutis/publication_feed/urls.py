from django.urls import path

from publication_feed import views

app_name = 'publication_feed'

urlpatterns = [
    path('publication_feed/', views.index, name='pub_feed'),
]