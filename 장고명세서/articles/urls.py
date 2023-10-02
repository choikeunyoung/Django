from django.urls import path, include
from . import views

app_name = "article"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("index/<int:pk>/", views.detail, name="detail"),
    path("index/<int:pk>/delete/", views.delete, name="delete"),
    path("index/<int:pk>/update/", views.update, name="update"),
]