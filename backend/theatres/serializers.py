from rest_framework import serializers
from .models import Theatre,Screen

class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = "__all__"


class ScreenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Screen
        fields = "['id', 'screen_number']"