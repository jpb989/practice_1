from django.core.exceptions import ValidationError
from datetime import timedelta, datetime
from .models import Screen
def validate_showtime_overlap(showtime):
    overlapping_shows = Screen.objects.filter(
        screen=showtime.screen,
        date=showtime.date
    ).exclude(id=showtime.id)

    for existing_show in overlapping_shows:
        existing_start = existing_show.time
        existing_end = (datetime.combine(existing_show.date, existing_show.time) + 
                        timedelta(minutes=existing_show.movie.duration)).time()
        new_start = showtime.start
        new_end = (datetime.combine(showtime.date, showtime.time) + 
                   timedelta(minutes=showtime.movie.duration)).time()
        
        if(new_start < existing_end and new_end > existing_start):
            raise ValidationError(
                f"Showtime overlaps with an existing show: {existing_show.movie.title} at {existing_show.time}"
            )