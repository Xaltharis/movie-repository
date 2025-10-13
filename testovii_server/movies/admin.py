from django.contrib import admin
from .models import Movie, Director, Genre, Actor

# admin.site.register(Movie)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    # Поля, которые будут отображаться в списке объектов
    list_display = ('id', 'title', 'release_date', 'country')

    # Поля, которые будут ссылками на страницу редактирования
    list_display_links = ('id', 'title')

    # Поля, по которым можно будет фильтровать
    list_filter = ('is_published', 'release_date', 'country')

    # Поля, по которым будет работать поиск
    search_fields = ('title', 'description', 'director')

    # Автоматическое заполнение слага на основе другого поля
    prepolutated_fields = {"slug": ("title")}

    filter_horizontal = ('Actor',)

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date')
    search_fields = ('first_name', 'last_name')