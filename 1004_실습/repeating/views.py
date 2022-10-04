from django.shortcuts import render


def index(request):
    return render(request, "repeating/index.html")
