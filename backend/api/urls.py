
from django.urls import path
from .views import RegisterApi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# This is the list of URL patterns Django will look for in this app.
urlpatterns = [
    path('register/', RegisterApi.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
