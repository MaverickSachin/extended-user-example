from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=1000, blank=True)
    bio = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f"Profile({self.user.username})"
