from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def log_in(request):
    form = UserCreationForm()
    context = {
        'form' : form
    }
    return render(request, "detail_info/login.html", context)