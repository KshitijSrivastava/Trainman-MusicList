from django.contrib import admin
from movie.models import Movie, MovieWatchList
# Register your models here.

admin.site.register(Movie)
admin.site.register(MovieWatchList)
