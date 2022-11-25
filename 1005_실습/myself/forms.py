from django import forms
from .models import Myself


class MyselfForm(forms.ModelForm):
    class Meta:
        model = Myself
        fields = ["title", "content"]
        labels = {
            "title": "제목",
            "content": "내용",
        }
