from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipients"
    )
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="actors")
    verb = models.CharField(max_length=255)
