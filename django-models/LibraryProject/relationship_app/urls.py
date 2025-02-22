from django.urls import path
from django.contrib.auth import views as auth_views

from .views import list_books
from .views import LibraryDetailView
from .views import SignUpView
from .views import LoginView
from .views import LogoutView


urlpatterns = [
    path("", list_books, name="list_books"),
    path("library/<pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("relationship_app/login", LoginView.as_view(), name="login"),
    path("relationship_app/logout/", LogoutView.as_view(), name="logout"),
    path("relationship_app/register/", SignUpView.as_view(), name="register"),
]
