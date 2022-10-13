from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'log'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('articles/', views.show, name='show'),
    path('login/', views.log_in, name="log_in"),
    path("", views.log_out, name="log_out"),
]