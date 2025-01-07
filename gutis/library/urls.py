from django.urls import path
from library.views import *

app_name = 'library'

urlpatterns = [
    path('semester_manuals/', semester_manuals , name='semester_manuals'),
    path('find_tutorial/', find_tutorial, name='find_tutorial'),
]