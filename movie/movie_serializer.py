from rest_framework import serializers

from movie.models import Movie


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["title", "categories", "year", "deleted"]


class MovieWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["title", "description", "image", "categories", "year", "deleted"]
