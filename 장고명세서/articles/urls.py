from django.urls import path, include
from . import views

app_name = "article"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("index/<int:pk>/", views.detail, name="detail"),
]