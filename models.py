from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # username and email are already included in AbstractUser
    email = models.EmailField(unique=True, max_length=255)
    phone = models.CharField(
        max_length=20, 
        blank=True, 
        null=True, 
        help_text="User's phone number"
    )

    # Use email or username for string representation
    def __str__(self):
        return self.username
