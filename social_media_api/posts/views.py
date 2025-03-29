from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .models import Post
from .serializer import PostSerializer


# Create your views here.
class PostListApiView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

