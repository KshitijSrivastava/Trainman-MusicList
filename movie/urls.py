from django.urls import path, include

from movie import views

urlpatterns = [
    path('populate-db', views.PopulateDB.as_view(), name ='populate-db'),
    path('movies', views.ListMovies.as_view(), name = 'movies-list'),
]
