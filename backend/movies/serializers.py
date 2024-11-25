from django.conf import settings
from rest_framework import serializers
from .models import Movie
class MovieListSerializer(serializers.ModelSerializer):
    poster = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id","title", "poster", "release_date", "rating"]
        
    def get_poster(self, obj):
        base_url = settings.MEDIA_DOMAIN
        print(settings.MEDIA_DOMAIN)
        if obj.poster:
            return f"{base_url}{obj.poster.url.lstrip('/')}"
        return None
        

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
    
    def get_poster(self, obj):
        base_url = settings.MEDIA_DOMAIN
        print(settings.MEDIA_DOMAIN)
        if obj.poster:
            return f"{base_url}{obj.poster.url.lstrip('/')}"
        return None