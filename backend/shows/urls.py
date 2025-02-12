from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShowView, BookingView

router = DefaultRouter()
router.register(r"shows", ShowView, basename="show")
router.register(r"bookings", BookingView, basename="booking")

urlpatterns = [
    path("", include(router.urls)),
]
