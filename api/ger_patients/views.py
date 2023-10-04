from rest_framework import viewsets
from .models import Therapist
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Therapist.objects.all()
    serializer_class = PatientSerializer