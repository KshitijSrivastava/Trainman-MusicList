from django.urls import path, include

from movie import views

urlpatterns = [
    path('populate-db', views.PopulateDB.as_view(), name ='populate-db'),
    path('movies', views.ListMovies.as_view(), name = 'movies-list'),
    path('user-movie-list', views.UserMovieList.as_view(), name ='user-movie-list'),
    path('watchlist-add', views.UserMovieAddUpdate.as_view(), name = 'watchlist-add'),
]
