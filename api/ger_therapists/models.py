from django.db import models
from api.models import User

class Therapist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100, null=True)
    # Add more fields as needed