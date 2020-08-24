from movie.models import MovieWatchList, Movie
from django.contrib.auth.models import User

class UserMoviesService():
    def __init__(self, request_data, user):
        self.data = request_data['data']
        self.user = user

    def extract_data_and_save(self):
        for slot in self.data:
            self.extract_each_data_and_save(slot)

    def extract_each_data_and_save(self, slot):
        try:
            movie_ = slot['movie']
            watched_ = slot['watched']
        except:
            return
        self.save_movie_watchlist(movie_str = movie_, watched = watched_)

    def save_movie_watchlist(self, movie_str, watched):
        print(movie_str, "|")
        try:
            user = User.objects.get(username = self.user)
            movie = Movie.objects.get(name = 'The Terminator (1984) ')
            print('The Godfather (1972) ', movie_str)
            #Movie.objects.get(name = str(movie_str))
        except:
            print(123456789)
            return
        print(movie, user, 'save_movie_watchlist')
        try:
            watchlist_movie = MovieWatchList.objects.get(
                movie = movie, user = user
            )
            watchlist_movie.watched = watched
            watchlist_movie.save()
        except:
            watchlist_movie = MovieWatchList(
                movie = movie, watched = watched, user = user)
            watchlist_movie.save()