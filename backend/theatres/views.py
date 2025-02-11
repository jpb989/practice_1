from rest_framework.views import APIView
from django.utils.dateparse import parse_date
from rest_framework.response import Response
from rest_framework import status

from .models import Theatre, Screen
from .serializers import TheatreSerializer





class ScreenView(APIView):
    def get(self, request, screen_id):
        try:
            screen = Screen.objects.filter()
        except:
            pass
