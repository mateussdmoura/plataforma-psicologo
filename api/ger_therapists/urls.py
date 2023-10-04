from rest_framework.routers import DefaultRouter
from .views import TherapistViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'therapists', TherapistViewSet, basename='therapist')

urlpatterns = [
    path('', include(router.urls)),
]