from django.urls import path
from rest_framework.authtoken import views
from .views import CustomAuthToken


urlpatterns = [
    path("api-token-auth/", CustomAuthToken.as_view()),
]
