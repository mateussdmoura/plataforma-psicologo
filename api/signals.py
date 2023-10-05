from django.db.models.signals import post_save
from django.dispatch import receiver
from api.ger_patients.models import Patient 
from api.models import User
from api.ger_therapists.models import Therapist

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_therapist:
            # Check if a Therapist instance already exists for this user
            therapist, _created = Therapist.objects.get_or_create(user=instance)
            if _created:
                # Perform additional setup for a new Therapist instance if needed
                pass
        else:
            Patient.objects.create(user=instance)
