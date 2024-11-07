from drf_spectacular.utils import OpenApiResponse

# Define the examples and descriptions for the API responses

logout_response_200_example = OpenApiResponse(
    description="Successfully blacklisted the token.",
    examples={
        'application/json': {
            'success': 'Token has been blacklisted.'
        }
    }
)

logout_response_400_example = OpenApiResponse(
    description="Invalid or expired token.",
    examples={
        'application/json': {
            'error': 'Token has already expired.'
        },
        'application/json': {
            'error': 'Token is required.'
        }
    }
)

logout_description = (
    "This endpoint blacklists the JWT token. "
    "Once blacklisted, the token can no longer be used to access protected endpoints."
)