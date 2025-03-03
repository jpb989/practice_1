from django.conf import settings
from rest_framework import serializers
from .models import Movie
from drf_spectacular.utils import extend_schema_field

class MovieListSerializer(serializers.ModelSerializer):
    poster = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id","title", "poster", "release_date", "rating"]
        
    def get_poster(self, obj):
        base_url = settings.MEDIA_DOMAIN
        print(settings.MEDIA_DOMAIN)
        if obj.poster_portrait:
            return f"{base_url}{obj.poster_portrait.url.lstrip('/')}"
        return None
        

class MovieSerializer(serializers.ModelSerializer):
    poster_portrait = serializers.SerializerMethodField()
    poster_landscape = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"

    @extend_schema_field(str)
    def get_poster_portrait(self, obj):
        base_url = settings.MEDIA_DOMAIN
        print(settings.MEDIA_DOMAIN)
        if obj.poster_portrait:
            return f"{base_url}{obj.poster_portrait.url.lstrip('/')}"
        return None
    
    @extend_schema_field(str)
    def get_poster_landscape(self, obj):
        base_url = settings.MEDIA_DOMAIN
        print(settings.MEDIA_DOMAIN)
        if obj.poster_landscape:
            return f"{base_url}{obj.poster_landscape.url.lstrip('/')}"
        return None