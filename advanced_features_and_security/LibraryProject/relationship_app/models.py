from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class CustomUserManager(BaseUserManager):
    def creat_user(self, email, password=None):
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.creat_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=256)
    date_of_birth = models.DateField(null=True)
    profile_photo = models.ImageField(upload_to=None)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_book", "can_add_book"),
            ("can_change_book", "can_change_book"),
            ("can_delete_book", "can_delete_book"),
        ]


class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(
        Library, on_delete=models.CASCADE, related_name="librarian"
    )

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    USER_ROLES = (
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member"),
    )

    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="userprofile"
    )
    role = models.CharField(max_length=255, choices=USER_ROLES)

    def __str__(self):
        return self.user.username + " " + self.role

    def create_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    post_save.connect(create_profile, sender=CustomUser)

    def update_profile(sender, instance, created, **kwargs):
        if created is False:
            instance.userprofile.save()

    post_save.connect(update_profile, sender=CustomUser)
