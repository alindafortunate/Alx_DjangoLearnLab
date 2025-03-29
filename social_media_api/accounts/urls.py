from django.urls import path
from rest_framework.authtoken import views
from .views import (
    CustomAuthToken,
    CustomUserLoginApiView,
    CustomUserRegistrationApiView,
    CustomUserLogoutApiView,
)


urlpatterns = [
    path("login/", CustomUserLoginApiView.as_view(), name="login"),
    path("register/", CustomUserRegistrationApiView.as_view(), name="register"),
    path("logout/", CustomUserLogoutApiView.as_view(), name="logout"),
    path("api-token-auth/", CustomAuthToken.as_view(), name="get-token"),
]
