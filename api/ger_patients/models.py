from django.db import models
from api.users.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add more fields as needed