from django.urls import path
from .views import ShowTimingsView

urlpatterns = [
    path("/show-timings/<str:date>", ShowTimingsView.as_view(), name="show-timings" ),
]
