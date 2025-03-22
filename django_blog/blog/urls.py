from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, profile

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
]
