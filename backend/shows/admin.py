from django.contrib import admin
from .models import ShowTime, Booking
# Register your models here.
admin.site.register(Booking)
admin.site.register(ShowTime)