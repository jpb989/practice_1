from rest_framework.views import APIView
from accounts.permission import IsStaffUser
from .models import Theatre, Seat, Screen
from .serializers import TheatreSerializer
from accounts.authentication import BlacklistTokenAuthentication
# Create your views here.
