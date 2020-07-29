from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>/", views.entry, name="entry"),
    path("wiki/create_page", views.create, name="create")
]
