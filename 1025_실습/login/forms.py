from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, ReadOnlyPasswordHashField, ReadOnlyPasswordHashWidget


class LoginForm(UserCreationForm):
    password1 = forms.CharField(
        label=("비밀번호"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text="",
    )
    password2 = forms.CharField(
        label=("비밀번호 확인"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="",
    )
    class Meta:
        model = get_user_model()
        fields = ['username',]
        help_texts = {
            'username' : "",
        }

class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(
        label=("Password"),
        help_text="",
    )
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name',]
        help_texts = {
            'username' : "",
        }