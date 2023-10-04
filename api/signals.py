from django.db.models.signals import post_save
from django.dispatch import receiver
from api.ger_patients.models import Patient 
from api.users.models import User
from api.ger_therapists.models import Therapist

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_therapist:
            Therapist.objects.create(user=instance)
        else:
            Patient.objects.create(user=instance)