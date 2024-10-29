from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiResponse

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

