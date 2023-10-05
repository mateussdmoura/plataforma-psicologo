from django.db import models
from api.models import User

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add more fields as needed
    
    def save(self, *args, **kwargs):
        # Check if the associated user has is_therapist set to True
        if self.user.is_therapist:
            raise ValueError("The associated user must have is_therapist set to False.")
        super().save(*args, **kwargs)