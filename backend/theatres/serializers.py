from rest_framework import serializers
from .models import Theatre, Seat, Screen, ShowTime

class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = "__all__"

class ShowTimeSerializer(serializers.ModelSerializer):
    theatre = serializers.CharField(source="screen.theatre.name")
    screen = serializers.CharField(source="screen.screen_number")
    movie_title = serializers.CharField(source="movie.title")
    
    class Meta:
        model = ShowTime
        fields = ["id", "theatre", "screen", "movie_title", "time", "date"]