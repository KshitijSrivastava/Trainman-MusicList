from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from .serializers import PopulateDBSerializer, MovieWatchSerializer
from .models import Movie, MovieWatchList
from .services.populate_db_services import PopulateDBService
from .services.user_movies_services import UserMoviesService
# Create your views here.


def index(request):
    return HttpResponse("Hello, world")

class ListMovies(APIView):

    def get(self, request, format=None):
        return_response = [ movie.to_json() for movie in Movie.objects.all()]
        return Response(return_response , status=status.HTTP_200_OK)

class PopulateDB(APIView):

    def post(self, request, format=None):

        serializer = PopulateDBSerializer(data=request.data)
        if serializer.is_valid():
            obj = PopulateDBService(serializer.data)
            obj.populate()
        return Response({"status": "DB is populated"} , status=status.HTTP_200_OK)


"2343eab28cb1089c97b1749f6ef4dc5297f741a9"



class UserMovieList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = User.objects.get(username = str(request.user))
        return_response = [ movie.to_json() for movie in MovieWatchList.objects.filter(
            user = user
        )]

        return Response(return_response)


class UserMovieAddUpdate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):

        serializer = MovieWatchSerializer(data=request.data)
        if serializer.is_valid():
            obj = UserMoviesService(serializer.data, user = str(request.user))
            obj.extract_data_and_save()
            return Response( "Added/Updated the list" , status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)