from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from accounts.authentication import BlacklistTokenAuthentication
from .models import Theatre, Screen, Seat
from .serializers import TheatreSerializer, ScreenSerializer, SeatSerializer
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

class TheatreView(viewsets.ModelViewSet):
    queryset = Theatre.objects.all()
    permission_classes = [AllowAny]
    authentication_classes = [BlacklistTokenAuthentication]
    serializer_class = TheatreSerializer

class ScreenView(viewsets.ModelViewSet):
    queryset = Screen.objects.all()
    permission_classes = [AllowAny]
    authentication_classes = [BlacklistTokenAuthentication]
    serializer_class = ScreenSerializer


class SeatView(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [AllowAny]
    authentication_classes = [BlacklistTokenAuthentication]

    def get_queryset(self):
        """Optionally filters seats by screen."""
        screen_id = self.request.query_params.get('screen')
        if screen_id:
            return self.queryset.filter(screen_id=screen_id)
        return self.queryset

    @action(detail=False, methods=['post'])
    def bulk_create(self, request):
        """Creates seats in bulk for a specific screen."""
        screen_id = request.data.get('screen')
        empty_seats = request.data.get('empty_seats', [])
        row_labels = request.data.get('row_labels', [])
        col_labels = request.data.get('col_labels', [])

        screen = get_object_or_404(Screen, id=screen_id)
        Seat.create_seats_custom_label(screen, row_labels, col_labels, empty_seats)
        return Response({'message': 'Seats created successfully with custom labels'}, status=201)
