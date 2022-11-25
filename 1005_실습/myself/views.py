from django.shortcuts import redirect, render
from .models import Myself
from .forms import MyselfForm


def index(request):
    myselfs = Myself.objects.all().order_by("-pk")
    context = {"myselfs": myselfs}
    return render(request, "self/index.html", context)


def new(reuqest):
    myself_form = MyselfForm()
    context = {
        "myself_form": myself_form,
    }
    return render(reuqest, "self/new.html", context)


def create(request):
    Myself.objects.create(
        title=request.POST.get("title"), content=request.POST.get("content")
    )
    return redirect("self:index")
