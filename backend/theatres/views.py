from rest_framework.views import APIView
from django.utils.dateparse import parse_date
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from accounts.authentication import BlacklistTokenAuthentication
from .models import Theatre, Screen
from .serializers import TheatreSerializer

class TheatreView(viewsets.ModelViewSet):
    queryset = Theatre.objects.all()
    permission_classes = [AllowAny]
    authentication_classes = [BlacklistTokenAuthentication]
    serializer_class = TheatreSerializer
