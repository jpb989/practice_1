from rest_framework import serializers
from .models import Theatre, Screen, Seat

class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = "__all__"


class ScreenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Screen
        fields = ['id', 'screen_number']

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'screen', 'row_position', 'column_position', 'seat_label']
        read_only_fields = ['seat_label']