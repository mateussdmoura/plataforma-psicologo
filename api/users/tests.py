from api.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.ger_therapists.models import Therapist
from api.ger_patients.models import Patient
import uuid  # Import the uuid module

class UserViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def generate_unique_username(self):
        # Generate a unique username using a UUID
        return f"user_{uuid.uuid4().hex[:10]}"  # Example: user_a1b2c3d4e5

    def test_create_therapist(self):
        username = self.generate_unique_username()  # Generate a unique username
        data = {
            "username": username,
            "password": "testpassword",
            "is_therapist": True
        }
        response = self.client.post('/api/users/', data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if a User and Therapist instance were created
        self.assertTrue(User.objects.filter(username=username).exists())
        self.assertTrue(Therapist.objects.filter(user__username=username).exists())
    
    def test_create_patient(self):
        username = self.generate_unique_username()  # Generate a unique username
        data = {
            "username": username,
            "password": "testpassword",
            "is_therapist": False
        }
        response = self.client.post('/api/users/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if a User and Patient instance were created
        self.assertTrue(User.objects.filter(username=username).exists())
        self.assertTrue(Patient.objects.filter(user__username=username).exists())
