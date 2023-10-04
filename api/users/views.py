from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer
from api.ger_therapists.models import Therapist
from api.ger_patients.models import Patient

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Save the user instance
        self.perform_create(serializer)
        
        # Check if the created user is a therapist or a patient
        is_therapist = serializer.validated_data.get('is_therapist', False)
        user = serializer.instance
        
        # Create a therapist or patient instance accordingly
        if is_therapist:
            Therapist.objects.create(user=user)
        else:
            Patient.objects.create(user=user)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
