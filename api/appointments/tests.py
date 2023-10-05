from django.test import TestCase
from django.utils import timezone
from datetime import date
from api.ger_patients.models import Patient
from api.ger_therapists.models import Therapist
from appointments.models import Appointment, AppointmentState
from api.models import User

class AppointmentTestCase(TestCase):
    def setUp(self):
        # Create a user for the patient
        self.patient_user = User.objects.create(
            username="patient",
            password="password",
            email="patient@test.com",
            date_of_birth=date(1990, 1, 1),
        )

        # Create a user for the therapist
        self.therapist_user = User.objects.create(
            username="therapist",
            password="password",
            email="therapist@test.com",
            date_of_birth=date(1980, 1, 1),
            is_therapist=True,
        )

        # Fetch the patient using the patient user
        self.patient = Patient.objects.get(user=self.patient_user)

        # Fetch the therapist using the therapist user
        self.therapist = Therapist.objects.get(user=self.therapist_user)

    def test_create_appointment(self):
        # Create an appointment
        appointment = Appointment.objects.create(
            start_time=timezone.now(),
            end_time=timezone.now() + timezone.timedelta(hours=1),
            patient=self.patient,
            therapist=self.therapist,
            requested_by=self.patient_user,  # Specify the user who requested the appointment
            state=AppointmentState.SCHEDULED.value,
        )

        # Check if the appointment was created successfully
        self.assertIsNotNone(appointment)
        self.assertEqual(appointment.patient, self.patient)
        self.assertEqual(appointment.therapist, self.therapist)
        self.assertEqual(appointment.requested_by, self.patient_user)  # Verify the requester
        self.assertEqual(appointment.state, AppointmentState.SCHEDULED.value)
