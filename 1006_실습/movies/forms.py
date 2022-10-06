from django import forms
from .models import Movie_Info

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie_Info
        fields = ['title', 'summary', 'running_time']
        label = {
            'title' : 'Title',
            'summary' : 'Summary',
            'running_time' : 'Running_time',
        }
        Value = {
            'title' : 'Title',
            'summary' : 'Summary',
            'running_time' : 0,
        }