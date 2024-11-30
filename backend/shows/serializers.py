from rest_framework import serializers
from .models import ShowTime


class ShowTimeSerializer(serializers.ModelSerializer):
    theatre = serializers.CharField(source="screen.theatre.name")
    screen_name = serializers.CharField(source="screen.screen_number")
    screen_id = serializers.CharField(source="screen.id")
    movie_title = serializers.CharField(source="movie.title")
    available_seats = serializers.SerializerMethodField()
    
    class Meta:
        model = ShowTime
        fields = ["id", "theatre", "screen_name", "screen_id", "movie_title", "time", "date", "available_seats"]
