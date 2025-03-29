from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment
from .serializer import PostSerializer, CommentSerializer


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
