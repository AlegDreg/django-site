from rest_framework import serializers
from . import models


class Title_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Title
        fields = '__all__'

class Volume_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Volume
        fields = '__all__'

class Chapter_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chapter
        fields = '__all__'

class Title_info_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Title_info
        fields = ('id','description','tag','ru_name', 'en_name', 'alt_name')
