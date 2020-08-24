from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PopulateDBSerializer
from .models import Movie
from .services.populate_db_services import PopulateDBService
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
