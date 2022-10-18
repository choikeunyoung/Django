from django import forms
from .models import Article
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