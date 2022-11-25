from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from .models import User

def log_in(request):
    # POST 요청 처리
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info:list')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, "detail_info/login.html", context)


def user_list(request):
    form = User.objects.all()
    context = {
        "forms" : form
    }
    return render(request, 'detail_info/list.html', context)