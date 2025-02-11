from rest_framework.views import APIView
from django.utils.dateparse import parse_date
from rest_framework.response import Response
from rest_framework import status

from .models import Show
from .serializers import ShowTimeSerializer


class ShowTimingView(APIView):
    def get(self, request, date):
        try:
            show_date  = parse_date(date)
            if not show_date:
                raise ValueError
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)
        
        showtimes = Show.objects.filter(date=show_date).select_related("movie", "screen__theatre")
        serializer = ShowTimeSerializer(showtimes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)