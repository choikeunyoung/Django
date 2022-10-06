from django.shortcuts import render, redirect
from traitlets import Instance
from .models import Movie_Info
from .forms import MovieForm

def main(request):
    return render(request, 'movie_info/main.html')

def board(request):
    movies = Movie_Info.objects.all().order_by('-pk')
    movies_len = []
    c = 1
    for i in movies:
        movies_len.append({'pk': i.pk, 'title': i.title , 'summary':i.summary, 'running_time':i.running_time, 'num': c})
        c+= 1
    context = {
        'movies' : movies_len,
    }
    return render(request, 'movie_info/board.html', context)

def create(request):
    if request.method == 'POST':
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
            return redirect('movie_info:board')
    else:
        movies_form = MovieForm()
    context = {
        'movies_form' : movies_form
    }
    return render(request, 'movie_info/new.html', context=context)

def details(request, pk):
    movie_info = Movie_Info.objects.get(pk=pk)
    context = {
        'movie_info' : movie_info
    }
    return render(request, 'movie_info/details.html', context)

def edit(request, pk):
    movie_info = Movie_Info.objects.get(pk=pk)
    if request.method == 'POST':
        movie_form = MovieForm(request.POST, instance=movie_info)
        if movie_form.is_valid():
            movie_form.save()
            return redirect("movie_info:details", movie_info.pk)
    else:
        movie_form = MovieForm(instance=movie_info)
    context = {
        'movie_info' : movie_info,
        'movie_form' : movie_form,
    }
    return render(request, 'movie_info/edit.html', context)

def delete(request, pk):
    movie_info = Movie_Info.objects.get(pk=pk)
    movie_info.delete()
    return redirect("movie_info:board")