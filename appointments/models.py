from django.db import models
from api.ger_therapists.models import Therapist
from api.ger_patients.models import Patient
from enum import Enum

class AppointmentState(Enum):
    SCHEDULED = 'Scheduled'
    ONGOING = 'Ongoing'
    CANCELLED = 'Cancelled'
    DONE = 'Done'

class Appointment(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    state = models.CharField(
        max_length=20,
        choices=[(state.value, state.name) for state in AppointmentState],
        default=AppointmentState.SCHEDULED.value
    )
