from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(help_text="The user's email address.")
    name = serializers.CharField(max_length=255, help_text="The user's name.")
    password = serializers.CharField(write_only=True, help_text="The user's password.")
    confirm_password = serializers.CharField(write_only=True, help_text="Confirm the user's password.")
    avatar = serializers.ImageField(required=False, help_text="Optional avatar image.")

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Passwords do not match")
        if User.objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError("A user with this email already exists")
        return data

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        validated_data["password"] = make_password(validated_data["password"])
        user = User.objects.create(**validated_data)
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        # ...

        return token
    
class LogoutSerializer(serializers.Serializer):
    token = serializers.CharField(help_text="JWT token to be blacklisted.")

