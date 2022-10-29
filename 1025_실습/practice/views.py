from django.shortcuts import get_object_or_404, redirect, render
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os

@login_required(login_url="log:log_in")
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
    user_info = get_user_model().objects.all()
    
    context = {
        'forms' : form
    }
    return render(request, "articleprac/article.html", context)

def detail(request, pk):
    form_detail = Article.objects.get(pk=pk)
    user_info = get_user_model().objects.get(pk=form_detail.user_id)
    comment_form = CommentForm()
    comments = form_detail.comment_set.all()
    context = {
        'form' : form_detail,
        'user_info' : user_info,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, "articleprac/detail.html", context)

@login_required(login_url="log:log_in")
def delete(request, pk):
    form = Article.objects.get(pk=pk)
    if form.image:
        os.remove(form.image.path)
    Article.delete(form)
    return redirect("prac:article")


@login_required(login_url="log:log_in")
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


@login_required(login_url="log:log_in")
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

# @login_required(login_url="log:log_in")
# def comment_edit(request, article_pk, comment_pk):
#     article = Comment.objects.get(pk=comment_pk)
#     comment_form = CommentForm(instance=article)
#     if request.method == 'POST':
#         edit_form = CommentForm(request.POST, instance=comment_form)

@login_required(login_url="log:log_in")
def likes(request, pk):
    # 로그인한 유저인지 확인
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        # like_users에 pk값이 존재하는지 필터로 확인
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
            article.like_count -= 1
            article.save()
        else:
            article.like_users.add(request.user)
            article.like_count += 1
            article.save()
        return redirect("prac:detail", article.pk)
    return redirect("log:log_in")


@login_required(login_url="log:log_in")
def follower(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        following_user = get_user_model().objects.get(pk=article.user_id)
        if request.user.pk == article.user_id:
            messages.warning(request, "스스로 팔로우 할 수 없습니다.")
            return redirect("prac:detail", pk)
        else:
            if request.user in following_user.followings.all():
                following_user.followings.remove(request.user.pk)
            elif request.user not in following_user.followings.all():
                following_user.followings.add(request.user.pk)
            return redirect("prac:detail", article.pk)
    return redirect("log:log_in")

@login_required(login_url="log:log_in")
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('prac:detail', article_pk)


def main(request):
    return render(request, "articleprac/main.html")

def main2(request):
    return render(request, "articleprac/main2.html")