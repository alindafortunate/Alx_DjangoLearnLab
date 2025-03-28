from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User should an email.")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    username = models.CharField(unique=False, max_length=100)
    email = models.EmailField(unique=True, max_length=200)
    bio = models.TextField(max_length=255)
    profile_picture = models.ImageField()
    followers = models.ManyToManyField(User, symmetrical=False)

    USERNAME_FIELD = "email"

    objects = CustomUserManager()
