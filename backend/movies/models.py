from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    language = models.CharField(max_length=50)
    release_date = models.DateField()
    poster_portrait = models.ImageField(upload_to="movie_posters/poster_portrait/", null=True, blank=True)
    poster_landscape = models.ImageField(upload_to="movie_posters/poster_landscape/", null=True, blank=True)
    trailer = models.URLField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        null=True, 
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    def __str__(self):
        return self.title


