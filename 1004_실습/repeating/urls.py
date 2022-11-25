"""repeat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from repeating import views

app_name = "repeating"

urlpatterns = [
    # localhost8000/repeating/
    path("", views.index, name="index"),
    # localhost8000/repeating/new/
    path("new/", views.new, name="new"),
    # localhost8000/repeating/create/
    path("create/", views.create, name="create"),
    # name을 지정해주는 이유는 변수화를 하기 위해서이다.
    path("edit/<int:pk>/", views.edit, name="edit"),
    # edit 한 값을 넘겨주는 길 생성
    path("editing/<int:pk>/", views.editing, name="editing"),
]
