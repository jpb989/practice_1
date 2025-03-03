import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import User
from .redis_client import redis_instance
from drf_spectacular.extensions import OpenApiAuthenticationExtension

class BlacklistTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")
        print(f"header: {auth_header}")
        if not auth_header:
            return None
        
        try:
            # Extract token from the header
            token = auth_header.split()[1]
            
            # Decode the token
            decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired.")
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid token.")
        
        # Check if the token is blacklisted in Redis
        if redis_instance.exists(token):
            raise AuthenticationFailed("Token is blacklisted.")

        # Extract user information from the decoded data
        user_id = decoded_data.get("user_id")
        
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise AuthenticationFailed("User not found.")
        
        return (user, token)

class BlacklistTokenAuthenticationScheme(OpenApiAuthenticationExtension):
    target_class = BlacklistTokenAuthentication
    name = 'BlacklistToken'
    
    def get_security_definition(self, auto_schema):
        return {
            'type': 'http',
            'scheme': 'bearer',
            'bearerFormat': 'JWT'
        }