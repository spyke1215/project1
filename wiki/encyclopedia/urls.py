from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/CSS/", views.css, name="css"),
    path("wiki/Django/", views.django, name="django"),
    path("wiki/Git/", views.git, name="git"),
    path("wiki/HTML/", views.html, name="html"),
    path("wiki/Python/", views.python, name="python")
]
