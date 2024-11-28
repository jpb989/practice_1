from rest_framework.views import APIView
from accounts.permission import IsStaffUser
from django.utils.dateparse import parse_date
from rest_framework.response import Response
from rest_framework import status

from .models import Theatre, Seat, Screen, ShowTime
from .serializers import TheatreSerializer, ShowTimeSerializer
from accounts.authentication import BlacklistTokenAuthentication
# Create your views here.

class ShowTimingsView(APIView):
    def get(self, request, date):
        try:
            show_date  = parse_date(date)
            if not show_date:
                raise ValueError
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)
        
        showtimes = ShowTime.objects.filter(date=show_date).select_related("movie", "screen__theatre")
        serializer = ShowTimeSerializer(showtimes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
