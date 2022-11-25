from urllib.request import Request
from django.shortcuts import redirect, render

from .models import Repeating  # 모델로 정의한 DB 값을 불러오는 부분


def index(request):
    # DB에 저장된 값을 받아와 context로 넘겨주고 index.html에서 받아온다
    repeating = Repeating.objects.order_by("-pk")
    context = {"repeats": repeating}
    return render(request, "repeating/index.html", context)


def new(request):
    return render(request, "repeating/new.html")


def create(request):
    # DB에 값을 넣는 부분
    title = request.POST.get("title")  # title = request.GET.get("title")
    content = request.POST.get("content")  # content = request.GET.get("content")
    Repeating.objects.create(title=title, content=content)
    # redirect를 통하여 index.html 로 이동
    return redirect("repeating:index")


def edit(request, pk):
    # pk 값을 통하여 지정된 게시물의 title, content를 받아온다
    repeats = Repeating.objects.get(pk=pk)
    context = {
        "repeats": repeats,
    }
    # edit.html 로 값들을 넘겨준다
    return render(request, "repeating/edit.html", context)


def editing(request, pk):
    repeats = Repeating.objects.get(pk=pk)
    repeats.title = request.POST.get("title")
    repeats.content = request.POST.get("content")
    repeats.save()
    return redirect("repeating:index")
