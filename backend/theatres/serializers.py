from rest_framework import serializers
from .models import Theatre, Seat, Screen, ShowTime

class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = "__all__"


class SeatSerializer(serializers.ModelSerializer):
    seat_identifier = serializers.SerializerMethodField()

    class Meta:
        model = Seat
        fields = ['id', 'seat_identifier', 'is_available']

    def get_seat_identifier(self, obj):
        return f"{obj.row_name}{obj.column_number}"


class ScreenSerializer(serializers.ModelSerializer):
    seats = SeatSerializer(many=True, read_only=True)

    class Meta:
        model = Screen
        fields = ['id', 'name', 'seating_grid', 'seats']