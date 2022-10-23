from django.shortcuts import redirect, render
from traitlets import Instance
from .forms import LoginForm, CustomUserChangeForm
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

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
    if request.user.is_authenticated:
        return redirect("prac:article")
    
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(request.GET.get("next") or "prac:article")
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, "homepage/login.html", context)

@login_required(login_url="log:log_in")
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

@login_required(login_url="log:log_in")
def delete(request, pk):
    form = User.objects.get(pk=pk)
    form.delete()
    return redirect("prac:article")

@login_required(login_url="log:log_in")
def profile_detail(request, pk):
    form = User.objects.get(pk=pk)
    context = {
        'form' : form,
    }
    return render(request, "homepage/profile_info.html", context)

@login_required(login_url="log:log_in")
def log_out(request):
    logout(request)
    return redirect("prac:article")

@login_required(login_url="log:log_in")
def account_delete(request):
    request.user.delete()
    logout(request)
    return redirect("prac:article")