from django.db import models
from uuid import uuid4

def default_grid():
    return [[0] * 5 for _ in range(5)]

class Theatre(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Screen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, related_name="screens")
    screen_number = models.CharField(max_length=10)
    seating_grid = models.JSONField(default=default_grid)

    def __str__(self):
        return f"{self.theatre.name} - Screen {self.screen_number}"

    def get_total_seats(self):
        return sum(len(row) for row in self.seating_grid)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["theatre", "screen_number"], name="unique_theatre_screen_number")
        ]


class Seat(models.Model):
    screen = models.ForeignKey(Screen, related_name='seats', on_delete=models.CASCADE)
    row_name = models.CharField(max_length=2)  # A, B, C, etc.
    column_number = models.IntegerField()

    def __str__(self):
        return f"{self.row_name}{self.column_number}"


