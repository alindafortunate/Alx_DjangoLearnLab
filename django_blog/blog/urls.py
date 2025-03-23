from django.urls import path
from django.contrib.auth.views import LoginView
from .views import (
    index,
    register,
    profile,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    LogoutView,
    logout_view,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    path("", index, name="home"),
    path(
        "login/",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("logout/", logout_view, name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("posts/", PostListView.as_view(), name="posts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path(
        "post/<int:pk>/new/comment/", CommentCreateView.as_view(), name="comment-create"
    ),
    path(
        "post/<int:pk>/update/comment/",
        CommentUpdateView.as_view(),
        name="comment-update",
    ),
    path(
        "post/<int:pk>/delete/comment/",
        CommentDeleteView.as_view(),
        name="comment-delete",
    ),
]
