from django.contrib import admin
from .models import Theatre, Screen, Seat, ShowTime
# Register your models here.

admin.site.register(Theatre)
admin.site.register(Screen)
admin.site.register(Seat)
admin.site.register(ShowTime)