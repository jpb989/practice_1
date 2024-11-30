import jwt
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LogoutSerializer
from .api_docs import logout_description, logout_response_200_example, logout_response_400_example
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from .authentication import BlacklistTokenAuthentication
from django.conf import settings
from .redis_client import redis_instance
from rest_framework_simplejwt.views import TokenRefreshView

import datetime

class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get('refresh')
        if redis_instance.get(refresh_token) == "blacklisted":
            return Response({"detail": "This token has been blacklisted."}, status=status.HTTP_403_FORBIDDEN)
        return super().post(request, *args, **kwargs)


class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    @extend_schema(
        request=RegisterSerializer,
        responses={
            201: OpenApiResponse(
                description="User created Successfully",
                response=RegisterSerializer,  # Ensure the response is valid and named correctly
            )
        },
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
    permission_classes = [AllowAny]

    @extend_schema(
        request=LogoutSerializer,
        responses={
            200: logout_response_200_example,
            400: logout_response_400_example,
        },
        description=logout_description
    )
    def post(self, request):
        access_token = request.data.get("access")
        refresh_token = request.data.get("refresh")
        
        if not access_token and not refresh_token:
            return Response(
                {"error": "At least one token (access or refresh) is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        errors = []
        success = []

        # Helper function to blacklist token
        def blacklist_token(token_type, token):
            try:
                decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                expiration_time = decoded_data["exp"] - int(datetime.datetime.now().timestamp())
                redis_instance.setex(token, expiration_time, "blacklisted")
                success.append(f"{token_type} has been blacklisted.")
            except jwt.ExpiredSignatureError:
                errors.append(f"{token_type} has already expired.")
            except jwt.InvalidTokenError:
                errors.append(f"Invalid {token_type}.")
        
        if refresh_token:
            blacklist_token("refresh_token", refresh_token)
        if access_token:
            blacklist_token("access_token", access_token)

        # If no tokens were successfully blacklisted, return 400
        if not success:
            return Response(
                {"error": "Both tokens are invalid or expired."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Return the appropriate response if there were some successes
        return Response({"success": success, "errors": errors}, status=status.HTTP_200_OK)


