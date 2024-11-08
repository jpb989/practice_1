from drf_spectacular.extensions import OpenApiAuthenticationExtension
from .authentication import BlacklistTokenAuthentication

class BlacklistTokenAuthenticationExtension(OpenApiAuthenticationExtension):
    target_class = 'accounts.authentication.BlacklistTokenAuthentication'  # Full import path to your authentication class
    name = 'BlacklistTokenAuth'  # Unique name for your custom authentication

    def get_security_definition(self, auto_schema):
        return {
            'type': 'http',
            'scheme': 'bearer',
            'bearerFormat': 'JWT',
            'description': 'Blacklist Token Authentication'
        }
