from rest_framework import serializers


class PopulateDBSerializer(serializers.Serializer):
    url = serializers.URLField()
    
