from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

def log_in(request):
    # POST 요청 처리
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, "detail_info/login.html", context)