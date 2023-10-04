from rest_framework import serializers
from api.models import User
from api.ger_therapists.models import Therapist
from api.ger_patients.models import Patient

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'is_therapist']
    
    def create(self, validated_data):
        # Extract 'is_therapist' from validated data
        is_therapist = validated_data.pop('is_therapist', False)
        
        # Create the User instance
        user = User.objects.create_user(**validated_data)
        
        # Create a Therapist or Patient instance based on 'is_therapist'
        if is_therapist:
            Therapist.objects.create(user=user)
        else:
            Patient.objects.create(user=user)
        
        return user
