from rest_framework import serializers
from django.db import transaction
from .models import Show, Booking
from theatres.models import Seat

class ShowSerializer(serializers.ModelSerializer):
    movie_title = serializers.ReadOnlyField(source="movie.title")
    screen_number = serializers.ReadOnlyField(source="screen.screen_number")
    theatre_name = serializers.ReadOnlyField(source="screen.theatre.name")

    class Meta:
        model = Show
        fields = ["id", "screen", "movie", "movie_title", "screen_number", "theatre_name", "start_time", "end_time"]


class BookingSerializer(serializers.ModelSerializer):
    seats = serializers.PrimaryKeyRelatedField(queryset=Seat.objects.all(), many=True)

    class Meta:
        model = Booking
        fields = ["id", "show", "seats", "user", "booking_time"]
        read_only_fields = ["id", "booking_time"]

    def validate(self, data):
        show = data["show"]
        seats = data["seats"]

        # Validate that all seats belong to the correct screen
        if not all(seat.screen == show.screen for seat in seats):
            raise serializers.ValidationError("All selected seats must belong to the same screen as the show.")

        return data

    def create(self, validated_data):
        show = validated_data["show"]
        seats = validated_data.pop("seats")

        with transaction.atomic():
            # Lock selected seats to prevent race conditions
            locked_seats = Seat.objects.select_for_update().filter(id__in=[seat.id for seat in seats])

            # Ensure no locked seat is already booked for the given show
            already_booked = Booking.objects.filter(show=show, seats__in=locked_seats).exists()
            if already_booked:
                raise serializers.ValidationError("One or more selected seats are already booked for this show.")

            # Create booking safely
            booking = Booking.objects.create(**validated_data)
            booking.seats.set(seats)
            return booking
