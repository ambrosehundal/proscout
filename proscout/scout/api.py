from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import ProfileSerializer
from .models import Profile
from django.contrib.auth.models import User

class ProfileView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'homepage.html'


    def get(self, request, username=None):

        username = self.kwargs['username']

        user_id = User.objects.values_list('id', flat=True).get(username=username)

        user_profile = Profile.objects.filter(user=user_id)
        return Response({'profile':user_profile})

