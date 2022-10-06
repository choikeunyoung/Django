from django.shortcuts import render, redirect
from traitlets import Instance
from .models import Movie_Info
from .forms import MovieForm

def main(request):
    return render(request, 'movie_info/main.html')

def board(request):
    movies = Movie_Info.objects.all().order_by('-pk')
    context = {
        'movies' : movies,
    }
    return render(request, 'movie_info/board.html', context)

def new(request):
    movies_form = MovieForm()
    context = {
        'movies_form' : movies_form
    }
    return render(request, 'movie_info/new.html', context)

def create(request):
    Movie_Info.objects.create(title=request.POST.get('title'),summary=request.POST.get('summary'),running_time=request.POST.get('running_time'))
    return redirect("movie_info:board")

def details(request, pk):
    movie_info = Movie_Info.objects.get(pk=pk)
    context = {
        'movie_info' : movie_info
    }
    return render(request, 'movie_info/details.html', context)

def edit(request, pk):
    movie_info = Movie_Info.objects.get(pk=pk)
    context = {
        'title' : request.POST.get(Instance=movie_info.title),
        'summary' : request.POST.get(Instance=movie_info.summary),
        'running_time' : request.POST.get(Instance=movie_info.running_time),
    }
    return render(request, 'movie_info/edit.html', name='edit')
def delete(requet, pk):
    pass