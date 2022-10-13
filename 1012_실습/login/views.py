from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import loginForm


# login.html 에서 Form을 받아와볼 예정이기 때문에 forms.py에서 정의했던 loginForm을 import 해서 기존에 넘겨주던대로 login.html에 넘겨주기!

def signup(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log:show')
    else:
        form = loginForm()
    context = {
        'form' : form
    }
    return render(request, "loging/signup.html", context)

def show(request):
    form = get_user_model().objects.all()
    context = {
        'form' : form,
    }
    return render(request, "loging/articles.html", context)

def log_in(request):
    if request.method == 'POST':
        forms = AuthenticationForm(request, data=request.POST)
        if forms.is_valid():
            login(request, forms.get_user())
            return redirect('log:show')
    else:
        forms = AuthenticationForm()
    content = {
        'form' : forms
    }
    return render(request, "loging/login.html", content)

def log_out(request):
    logout(request)
    return redirect('log:show')