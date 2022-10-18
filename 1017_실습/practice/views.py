from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm


def index(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("prac:article")
    form = ArticleForm
    context = {
        'form' : form
    }
    return render(request, "articleprac/index.html", context)


def article(request):
    form = Article.objects.all()
    context = {
        'forms' : form
    }
    return render(request, "articleprac/article.html", context)

def detail(request, pk):
    form_detail = Article.objects.get(pk=pk)
    context = {
        'form' : form_detail,
    }
    return render(request, "articleprac/detail.html", context)

def delete(request, pk):
    form = Article.objects.get(pk=pk)
    Article.delete(form)
    return redirect("prac:article")

def update(request, pk):
    form_info = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=form_info)
        if form.is_valid():
            form.save()
            return redirect("prac:detail", form_info.pk)
    else:
        form = ArticleForm(instance=form_info)
    context = {
        'form' : form,
        'form_info' : form_info,
    }
    return render(request, 'articleprac/edit.html', context)
    
def main(request):
    return render(request, "articleprac/main.html")