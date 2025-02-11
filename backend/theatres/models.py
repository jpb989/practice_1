from django.db import models
from django.core.exceptions import ValidationError


class Theatre(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Screen(models.Model):
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, related_name="screens")
    screen_number = models.CharField(max_length=10)
    num_rows = models.PositiveSmallIntegerField(default=10)
    num_cols = models.PositiveSmallIntegerField(default=10)

    def __str__(self):
        return f"{self.theatre.name} - Screen {self.screen_number}"

    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["theatre", "screen_number"], name="unique_theatre_screen_number")
        ]


class Seat(models.Model):
    screen = models.ForeignKey("Screen", on_delete=models.CASCADE, related_name="seats")
    row_position = models.PositiveSmallIntegerField()
    column_position = models.PositiveSmallIntegerField()
    seat_label = models.CharField(max_length=10, blank=True, help_text="Eg., A1, B2", unique=True)

    def __str__(self):
        return f"{self.screen.theatre.name} {self.screen.screen_number} {self.seat_label}"

    def clean(self):
        """Validate that seat_label is unique per screen and that row_position and column_position do not exceed screen dimensions."""
        if self.screen:
            if self.row_position >= self.screen.num_rows:
                raise ValidationError({"row_position": f"Row position exceeds max rows ({self.screen.num_rows - 1})."})
            if self.column_position >= self.screen.num_cols:
                raise ValidationError({"column_position": f"Column position exceeds max columns ({self.screen.num_cols - 1})."})
            if Seat.objects.filter(screen=self.screen, seat_label=self.seat_label).exists():
                raise ValidationError(f"Seat label '{self.seat_label}' already exists in this screen.")
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["screen", "seat_label"], name="unique_screen_seat_label")
        ]

    @classmethod
    def create_seats_custom_label(cls, screen, rows, cols, empty_seats=None):
        """Creates seats using custom row and column labels"""
        seats = []
        empty_seats = set(empty_seats) if empty_seats else set()
        row_index= 0
        for i in range(screen.num_rows):
            row_label = rows[row_index]
            col_index = 0
            for j in range(screen.num_cols):
                if (i, j) in empty_seats:
                    empty_seats.discard((i, j))
                    continue
                col_label = cols[col_index]
                seat_label = f"{row_label}{col_label}"
                seats.append(cls(screen=screen, row_position=i, column_position=j, seat_label=seat_label))
                col_index+=1
            row_index+=1

        cls.objects.bulk_create(seats)

    @classmethod
    def create_seats(cls, screen, empty_seats=None):
        """Auto-generates seats with alphabetical row labels and numeric column labels"""
        row_labels = [chr(65 + i) for i in range(screen.num_rows)]  # 'A', 'B', 'C'...
        col_labels = [str(i + 1) for i in range(screen.num_cols)]   # '1', '2', '3'...

        cls.create_seats_custom_label(screen, row_labels, col_labels, empty_seats)


