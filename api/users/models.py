from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add custom fields
    date_of_birth = models.DateField(null=True, blank=True)
    # Add more custom fields as needed

    def __str__(self):
        return self.username
