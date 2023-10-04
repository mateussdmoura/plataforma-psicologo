from django.db import models
from api.users.models import User

class Therapist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100, null=True)
    # Add more fields as needed