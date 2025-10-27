from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Movie, Genre, Director, Actor

def index(request):
    all_movies = Movie.objects.filter(is_published=True).order_by('-release_date')

    paginator = Paginator(all_movies, 4)

    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
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

def actor_detail(request, pk):

    actor = get_object_or_404(Actor, pk=pk)

    movies = actor.movies.filter(is_published=True)

    context = {
        'actor': actor,
        'movies_list': movies,
        'title': f'Информация об актере: {actor}'
    }

    return render(request, 'movies/actor_detail.html', context=context)