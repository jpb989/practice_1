import jwt
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from .authentication import BlacklistTokenAuthentication
from django.conf import settings
import datetime

class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    @extend_schema(
        request=RegisterSerializer,  # Automatically uses the serializer for request schema
        responses={201: OpenApiResponse(
            description="User created Successfully",
            response=serializers.Serializer,  # If you want to document the custom response type
        )},
        description="Register a new user.",
        summary="User Registration"
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(data={"message": "User created Successfully"}, status=status.HTTP_201_CREATED)

class LogoutView(APIView):
    authentication_classes = [BlacklistTokenAuthentication]
    def post(self, request):
        token = request.data.get("token")
        if not token:
            return Response({"error": "Token is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS265"])
            expiration_time = decoded_data["exp"] - int(datetime.datetime.now().timestamp())

            settings.redis_instance.setex(token, expiration_time, "blacklisted")
            return Response({"success": "Token has been blacklisted."}, status=status.HTTP_200_OK)
        
        except jwt.ExpiredSignatureError:
            return Response({"error": "Token has already expired."}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.InvalidTokenError:
            return Response({"error": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)