from rest_framework import serializers


class PopulateDBSerializer(serializers.Serializer):
    url = serializers.URLField()
    

class ValueSerializer(serializers.Serializer):
    movie = serializers.CharField()
    watched = serializers.BooleanField()


class MovieWatchSerializer(serializers.Serializer):
    data = serializers.ListField( 
        child = ValueSerializer())