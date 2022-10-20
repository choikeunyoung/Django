from django.shortcuts import redirect, render
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
import os

@login_required
def index(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect("prac:article")
    form = ArticleForm()
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
    comment_form = CommentForm()
    comments = form_detail.comment_set.all()
    context = {
        'form' : form_detail,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, "articleprac/detail.html", context)

def delete(request, pk):
    form = Article.objects.get(pk=pk)
    if form.image:
        os.remove(form.image.path)
    Article.delete(form)
    return redirect("prac:article")

def update(request, pk):
    form_info = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=form_info)
        if form.is_valid():
            if (form_info.image and request.FILES.get('image')) or request.POST.get('image-clear'):
                os.remove(form_info.image.path)
            form.save()
            return redirect("prac:detail", form_info.pk)
    else:
        form = ArticleForm(instance=form_info)
    context = {
        'form' : form,
        'form_info' : form_info,
    }
    return render(request, 'articleprac/edit.html', context)
    
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST, pk)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect('prac:detail', article.pk)
    else:
        return redirect('prac:detail', article.pk)

def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('prac:detail', article_pk)

def main(request):
    return render(request, "articleprac/main.html")