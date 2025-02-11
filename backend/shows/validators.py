from django.core.exceptions import ValidationError
from .models import Show


def validate_showtime_overlap(show):
    overlapping_shows = Show.objects.filter(
        screen=show.screen,             # Same screen
        start_time__lt=show.end_time,   # Existing show starts before the new show ends
        end_time__gt=show.start_time,   # Existing show ends after the new show starts
    ).exclude(id=show.id)               # Exclude the current show if updating

    # If overlapping shows exist, raise a validation error
    if overlapping_shows.exists():
        conflicts = "\n".join(
            f"{s.movie.title} ({s.start_time.strftime('%Y-%m-%d %H:%M')} - {s.end_time.strftime('%Y-%m-%d %H:%M')})"
            for s in overlapping_shows
        )
        raise ValidationError(
            f"This show overlaps with existing shows:\n{conflicts}"
        )