from django.urls import path

from .views import list_book, LibraryDetailView

urlpatterns = [
    path("", list_book, name="list_books"),
    path("library/<pk>/", LibraryDetailView.as_view(), name="library_detail"),
]
