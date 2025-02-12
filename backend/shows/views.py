from rest_framework.views import APIView
from django.utils.dateparse import parse_date
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from accounts.authentication import BlacklistTokenAuthentication
from .models import Show, Booking
from .serializers import ShowSerializer, BookingSerializer


class ShowView(viewsets.ReadOnlyModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
    permission_classes = [AllowAny]

class BookingView(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    authentication_classes = [BlacklistTokenAuthentication]
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        booking = self.get_object()
        if booking.user != request.user:
            return Response({"error": "You can only cancel your own bookings."}, status=status.HTTP_403_FORBIDDEN)
        booking.delete()
        return Response({"message": "Booking cancelled successfully."}, status=status.HTTP_204_NO_CONTENT)

