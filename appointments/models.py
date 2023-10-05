from django.db import models
from api.ger_therapists.models import Therapist
from api.ger_patients.models import Patient
from api.models import User
from enum import Enum
from django.utils import timezone  # Import the timezone module

class AppointmentState(Enum):
    REQUESTED = "REQUESTED"
    SCHEDULED = "SCHEDULED"
    ONGOING = "ONGOING"
    CANCELLED = "CANCELLED"
    DONE = "DONE"

class Appointment(models.Model):
    title = models.CharField(max_length=40, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    state = models.CharField(
        max_length=20,
        choices=[(state.value, state.name) for state in AppointmentState],
        default=AppointmentState.SCHEDULED.value
    )
    notes = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(default=timezone.now)    
    def save(self, *args, **kwargs):
        # Check if the requested_by field is not set
        if not self.requested_by:
            # You can access the user who sent the request using the request object
            user = kwargs.get('user')  # Assuming 'user' is passed in as a keyword argument
            if user:
                self.requested_by = user

    def __str__(self):
        return f"[{self.state}] Appointment for {self.patient} with {self.therapist}"