from django.urls import path
from . import views
from . import forms

app_name = "info"

urlpatterns = [
    # http://127.0.0.1:8000/
    path("login/", views.log_in, name="log"),
    path("list/", views.user_list, name="list"),
]
