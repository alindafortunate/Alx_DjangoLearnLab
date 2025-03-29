from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, PostViewSet, like, unlike

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="posts")
router.register(r"comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("", include(router.urls)),
    path("posts/<int:pk>/like/", like, name="like"),
    path("/posts/<int:pk>/unlike/", unlike, name="unlike"),
]
