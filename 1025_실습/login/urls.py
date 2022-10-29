from django.urls import include, path
from . import views

app_name = "log"

urlpatterns = [
    path("login/", views.log_in, name='log_in'),
    path("signup/", views.signup, name='signup'),
    path("update/", views.update, name='update'),
    path("profile_detail/<int:pk>/", views.profile_detail, name="profile_detail"),
    path("logout/", views.log_out, name='log_out'),
    path("accounts_delete/", views.account_delete, name="acc_delete"),
    path("", views.delete, name="delete"),
]
