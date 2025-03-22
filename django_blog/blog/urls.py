from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import index, register, profile, post_list

urlpatterns = [
    path("", index, name="home"),
    path(
        "login/",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("posts/", post_list, name="posts"),
]
