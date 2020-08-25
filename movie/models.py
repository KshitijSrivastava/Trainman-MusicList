from django.db import models
# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length = 100, )
    imdb_rating =  models.DecimalField(max_digits = 4, decimal_places = 2, null = True)
    summary_text = models.TextField(null = True)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'name': self.name,
            'imdb_rating': self.imdb_rating,
            'summary': self.summary_text
        }


class MovieWatchList(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null = True)
    watched = models.BooleanField()

    def __str__(self):
        return str(self.movie) + " - " + str(self.user)

    def to_json(self):
        return {
            'movie': self.movie,
            'watched': self.watched
        }