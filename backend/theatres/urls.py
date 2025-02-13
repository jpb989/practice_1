from django.urls import path, include
from .views import TheatreView, ScreenView, SeatView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"theatre", TheatreView, basename="theatre")
router.register(r"screen", ScreenView, basename="screen")
router.register(r"seat", SeatView, basename="seat")

urlpatterns = [
    path("", include(router.urls)),
]
