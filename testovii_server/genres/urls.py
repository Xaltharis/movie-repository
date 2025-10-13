from django.urls import path

from .views import index1

urlpatterns = [
    path('genres/', index1),
]