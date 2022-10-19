from django.shortcuts import redirect, render
from traitlets import Instance
from .forms import LoginForm, CustomUserChangeForm
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def signup(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("log:log_in")
    else:
        form = LoginForm()
    context = {
        'form':form,
    }
    return render(request, "homepage/signup.html", context)


def log_in(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("prac:article")
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, "homepage/login.html", context)

def update(request):
    if request.method=="POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("log:profile_detail", request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, "homepage/info.html", context)

def delete(request, pk):
    form = User.objects.get(pk=pk)
    form.delete()
    return redirect("prac:article")

def profile_detail(request, pk):
    form = User.objects.get(pk=pk)
    context = {
        'form' : form,
    }
    return render(request, "homepage/profile_info.html", context)

def log_out(request):
    logout(request)
    return redirect("prac:article")