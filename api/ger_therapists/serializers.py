from rest_framework import serializers
from .models import Therapist

class TherapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapist
        fields = '__all__'

    def create(self, validated_data):
        # Check if the associated user has is_therapist set to True
        user = self.context['request'].user
        if not user.is_therapist:
            raise serializers.ValidationError("The associated user must have is_therapist set to True.")

        # Create the Therapist instance
        therapist = Therapist(**validated_data)
        therapist.user = user  # Associate the user with the therapist
        therapist.save()
        return therapist