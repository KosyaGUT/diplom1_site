from django.urls import path
from study import views

app_name = 'study'

urlpatterns = [
    path("schedule/", views.schedule, name="schedule"),
    path("curriculum/", views.curriculum, name="curriculum"),
    path("student_council/", views.student_council, name="student_council"),
    path("group_files/", views.group_files, name="group_files"),

]