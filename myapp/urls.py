from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add_faculty/", views.add_faculty, name="add_faculty"),
    path("add_subject/", views.add_subject, name="add_subject"),
    path("add_class/", views.add_class, name="add_class"),
    path("generate_timetable/", views.generate_timetable_view, name="generate_timetable"),
]
