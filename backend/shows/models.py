from django.db import models
from movies.models import Movie
from theatres.models import Screen, Seat
from django.contrib.auth import get_user_model
from .validators import validate_showtime_overlap
from uuid import uuid4

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
        return f"{self.movie.title} - {self.screen.theatre.name} {self.screen} at {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}"

class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name="bookings")
    seats = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name="bookings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    booking_time = models.DateTimeField(auto_now_add=True)
