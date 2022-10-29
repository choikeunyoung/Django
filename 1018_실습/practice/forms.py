from dataclasses import fields
from django import forms
from .models import Article, Comment
from django import forms

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title','content','image']
        labels = {
            'title' : '제목',
            'content' : '내용',
            'image' : '이미지',
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content',]
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'cols': 40 , 'id' : 'valinfo'})
        }
        labels = {
        'content': '',
        }