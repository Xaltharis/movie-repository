from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Movie, Genre, Director

def index(request):
    movies = Movie.objects.filter(is_published=True)

    context = {
        'movies_list': movies,
        'title': "КиноКаталог - Главная"
    }
    return render(request, 'movies/index.html', context=context)

def index1(request):
    return HttpResponse("Это страница с жанрами")

def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)

    context = {
        'movie': movie,
        'title': f'Фильм {movie.title}'
    }

    return render(request, 'movies/movie_detail.html', context=context)

def movies_by_genre(request, pk):
    genre = get_object_or_404(Genre,pk=pk)
    movies = genre.movies.filter(is_published=True)

    context = {
        'movies_list': movies,
        'title': f'Фильмы в жанре: {genre.name}'
    }
    return render(request, 'movies/movies_list.html', context=context)

def movies_by_director(request, pk):
    director = get_object_or_404(Director, pk=pk)
    movies = director.movies.filter(is_published=True)

    context = {
        'movie_list': movies,
        'title': f'Фильмы режиссёра: {director}'
    }
    return render(request, 'movies/movie_list.html', context=context)