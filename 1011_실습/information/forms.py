from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class CustomUserCreationForm(UserCreationForm):
    # password1 = forms.CharField(
    #     label=("Password"),
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    #     help_text="지우기",
    # )
    # password2 = forms.CharField(
    #     label=("Password confirmation"),
    #     widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    #     strip=False,
    #     help_text="지우기2",
    # )
    class Meta:
        model = User
        fields = ('username',)