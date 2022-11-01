from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from App_auth.views import *

app_name = 'App_auth'

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name="registration"),
    path('register-2/', registerAPIView, name="registration"),
    path('login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
