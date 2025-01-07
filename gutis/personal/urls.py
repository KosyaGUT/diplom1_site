from django.urls import path
from personal.views import *

app_name = 'personal'

urlpatterns = [
    path("my_profile/", my_profile, name="my_profile"),
    path("diary/", diary, name="diary"),
    path("access_to_services/", access_to_services, name="access_to_services"),
    path("ordering_information/", ordering_information, name="ordering_information"),
    path("messages/", messages, name="messages"),
    path("technical_support/", technical_support, name="technical_support"),
]