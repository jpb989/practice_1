from django.db import models
from movies.models import Movie
from theatres.models import Screen, Seat
from django.contrib.auth import get_user_model
from .validators import validate_showtime_overlap
from uuid import uuid4
from django.core.exceptions import ValidationError

User = get_user_model()

class Show(models.Model):
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name="shows")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="shows")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        unique_together = ("screen", "movie", "start_time")
        constraints = [
            models.CheckConstraint(
                check=models.Q(start_time__lt=models.F("end_time")),
                name="check_start_time_before_end_time"
            ),
        ]

    def clean(self):
        validate_showtime_overlap(self)
        
        if self.end_time < self.start_time + self.movie.duration:
            raise ValidationError("End time must be at least movie duration long.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.movie.title} - {self.screen.theatre.name} {self.screen} at {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}"

class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name="bookings")
    seats = models.ManyToManyField(Seat, related_name="bookings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    booking_time = models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        if self.pk:
            existing_booking = Booking.objects.filter(show=self.show).exclude(pk=self.pk)
        else:
            existing_booking = Booking.objects.filter(show=self.show)
        
        booked_seats = Seat.objects.filter(bookings__in=existing_booking)
        seats_to_book = self.seats.all()
        conflicting_seats = booked_seats.filter(pk__in=seats_to_book.values_list('pk', flat=True))
        if conflicting_seats.exists():
            seat_labels = ", ".join(str(seat.seat_label) for seat in conflicting_seats)
            raise ValidationError(f"Seats {seat_labels} are already booked for this show.")
        
    def save(self, *args, **kwargs):
        if not self.pk:
            self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        seat_numbers = ", ".join(str(seat.seat_label) for seat in self.seats.all())
        return f"{self.show.movie.title} - {self.show.screen.theatre.name} Screen: {self.show.screen.screen_number} Seats: {seat_numbers}"