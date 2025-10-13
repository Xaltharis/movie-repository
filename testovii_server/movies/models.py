from django.db import models
from django.utils import timezone
from django.urls import reverse

class Director(models.Model):
    # Основная информация о директоре
    first_name = models.CharField(max_length=50, null=False, verbose_name="Имя")
    last_name = models.CharField(max_length=50, null=False, verbose_name="Фамилия")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Режиссер"
        verbose_name_plural = "Режиссеры"

class Genre(models.Model):
    # Жанр
    name = models.CharField(max_length=50, unique=True, null=False, verbose_name="Название жанра")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Actor(models.Model):
    # Актёр
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    birth_date = models.DateField(verbose_name="Дата рождения", default=timezone.now)
    photo = models.ImageField(upload_to='actor_photos/', verbose_name="Фото", null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Актёр"
        verbose_name_plural = "Актёры"

class Movie(models.Model):
    # Основная информация
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    poster = models.ImageField(upload_to='movie_posters/', verbose_name="Постер", null=True, blank=True)
    release_date = models.DateField(verbose_name="Дата выхода", default=timezone.now)

    # Детали фильма
    director = models.ForeignKey(Director, on_delete=models.PROTECT, related_name='movies', verbose_name='Режиссёр')
    genres = models.ManyToManyField(Genre, related_name='movies', verbose_name='Жанр')
    Actor = models.ManyToManyField(Actor, related_name='movies', verbose_name='Актёр')
    country = models.CharField(max_length=100, verbose_name="Страна")
    duration_in_minutes = models.PositiveIntegerField(verbose_name="Продолжительность (мин)", help_text="Укажите продолжительность фильма в минутах")

    # Финансовая информация
    budget = models.PositiveIntegerField(verbose_name="Бюджет", default=0, help_text="Укажите сумму в долларах США")
    fees_in_usa = models.PositiveIntegerField(verbose_name="Сборы в США", default=0, help_text="Укажите сумму в долларах США")
    fees_in_world = models.PositiveIntegerField(verbose_name="Сборы в мире", default=0, help_text="Укажите сумму в долларах США")

    # Рейтинг и служебная информация
    rating_imbd = models.FloatField(verbose_name="Рейтинг кинопоиск", default=0.0)
    is_published = models.BooleanField(verbose_name="Опубликовано", default=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"