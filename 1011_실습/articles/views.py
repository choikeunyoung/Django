from django.shortcuts import render
from information.forms import User

def index(request):
    form = User.objects.all()
    context = {
        'forms' : form
    }
    return render(request, "article/index.html", context)
