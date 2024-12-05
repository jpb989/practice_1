from django.db import models
from movies.models import Movie
from theatres.models import Screen, Seat
from .validators import validate_showtime_overlap
from uuid import uuid4


class ShowTime(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name="showtimes")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="showtimes")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("screen", "movie", "date", "start_time")
        constraints = [
            models.CheckConstraint(
                check=models.Q(start_time__lt=models.F("end_time")),
                name="check_start_time_before_end_time"
            ),
            models.CheckConstraint(
                check=models.Q(end_time__gte=models.ExpressionWrapper(
                    models.F('start_time') + models.F('movie__duration'), output_field=models.TimeField()
                )),
                name="check_showtime_duration_gte_movie_duration"
            ),
        ]

    
    def clean(self):
        validate_showtime_overlap(self)

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.movie.title} - {self.screen.theatre.name} {self.screen} at {self.time} on {self.date}"

class Booking(models.Model):
    showtime = models.ForeignKey(ShowTime, on_delete=models.CASCADE, related_name="bookings")
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("showtime", "seat")