from rest_framework import serializers
from scout.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'birth_date', 'height', 'weight', 'weight_units', 'hometown', 'country', 'disciplines', 'mma_experience_level', 'headline', 'summary', 'image', 'role']