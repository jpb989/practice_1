from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from accounts.views import CustomTokenRefreshView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
     # Admin Panel
    path("admin/", admin.site.urls),

    # API Documentation (Swagger, ReDoc)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Authentication APIs
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),

    # User Accounts APIs (Login, Register)
    path('api/accounts/', include("accounts.urls")),

    # Shows & Bookings APIs
    path('api/', include("shows.urls")),
    path('api/', include("theatres.urls")),

    # Movies APIs
    path('api/movies/', include("movies.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

