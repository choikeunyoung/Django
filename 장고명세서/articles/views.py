from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


def index(request):
    articles = Article.objects.all()
    context = {
        "articles" : articles,
    }
    return render(request, "articles/index.html", context)


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("article:detail", article.pk)
        return redirect("article:create")
    else:
        form = ArticleForm()
        context = {
            "form" : form,
        }
        return render(request, "articles/create.html", context)
    

def detail(request, pk):
    article = Article.objects.get(pk = pk)
    context = {
        "article" : article,
    }
    return render(request, "articles/detail.html", context)


def delete(request, pk):
    article = Article.objects.get(pk = pk)
    article.delete()
    return redirect("article:index")


def update(request, pk):
    article = Article.objects.get(pk = pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("article:detail", article.pk)
        return redirect("article:update", article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        "article" : article,
        "form" : form,
    }
    return render(request, "articles/update.html", context)