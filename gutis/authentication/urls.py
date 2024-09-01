from django.urls import path

from authentication import views

app_name = 'authentication'

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='reg'),
    path('login/', views.login, name='log'),
]
