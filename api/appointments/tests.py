from django.test import TestCase
from django.utils import timezone
from datetime import date
from api.ger_patients.models import Patient
from api.ger_therapists.models import Therapist
from appointments.models import Appointment, AppointmentState
from api.models import User
from datetime import datetime, timedelta
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status

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

class AppointmentViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.therapist_user = User.objects.create_user(username='therapist', password='testpassword', is_therapist=True)
        self.patient_user = User.objects.create_user(username='patient', password='testpassword')
        self.client.force_authenticate(user=self.therapist_user)

        # Create a therapist and a patient
        self.therapist = Therapist.objects.get(user=self.therapist_user)
        self.patient = Patient.objects.get(user=self.patient_user)

    def test_create_appointment(self):
        # Define the data for creating an appointment
        appointment_data = {
            "title": "Meeting with Client",
            "notes": "Discuss project details",
            "start_time": datetime.now().isoformat(),
            "end_time": (datetime.now() + timedelta(hours=1)).isoformat(),
            "therapist": self.therapist.id,
            "patient": self.patient.id,
        }

        # Send a POST request to create the appointment
        response = self.client.post(reverse('appointment-list'), appointment_data, format='json')

        # Check if the request was successful (status code 201 CREATED)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the appointment was created in the database
        self.assertTrue(Appointment.objects.filter(title="Meeting with Client").exists())