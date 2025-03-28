from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commented_by"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_created=True, null=True)

    def __str__(self):
        return f"{self.post}"


class Tag(models.Model):
    name = models.ManyToManyField(Post)
    tags = TaggableManager()
