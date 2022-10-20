from django.contrib import admin
from django.urls import path
from . import views

app_name='prac'

urlpatterns = [
    path("article/", views.article, name="article"),
    path("index/", views.index, name='index'),
    path("detail/<int:pk>/", views.detail, name='detail'),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("main/", views.main, name="main"),
    path("edit/<int:pk>/", views.update, name='edit'),
    path("comments/<int:pk>/", views.comment_create, name="comment_create"),
    path("<int:article_pk>/comments/<int:comment_pk>/delete/", views.comment_delete, name="comment_delete"),
]
