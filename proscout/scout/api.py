from rest_framework import generics
from rest_framework.response import Response 
from .serializers import ProfileSerializer
from .models import Profile
from django.contrib.auth.models import User

class ProfileView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    
    def get_queryset(self):

        username = self.kwargs['username']

        user_id = User.objects.values_list('id', flat=True).get(username=username)

        return Profile.objects.filter(user=user_id)

