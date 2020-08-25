from rest_framework import serializers
from django.contrib.auth.models import User


class PopulateDBSerializer(serializers.Serializer):
    url = serializers.URLField()
    

class ValueSerializer(serializers.Serializer):
    movie = serializers.CharField()
    watched = serializers.BooleanField()


class MovieWatchSerializer(serializers.Serializer):
    data = serializers.ListField( 
        child = ValueSerializer())

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,)
    username = serializers.CharField()
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')