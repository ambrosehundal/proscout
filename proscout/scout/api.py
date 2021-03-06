from rest_framework import generics
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import ProfileSerializer
from .models import Profile
from django.contrib.auth.models import User
from scout.forms import UserProfileForm

class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'homepage.html'


    def get(self, request, username=None):
              
        print(request.user)

        username = self.kwargs['username']
        user_id = User.objects.values_list('id', flat=True).get(username=username)
        user_profile = Profile.objects.filter(user=user_id).first()

        if request.user.is_authenticated and username == str(request.user):
            user_id = User.objects.values_list('id', flat=True).get(username=request.user)
            authenticated_user_profile = Profile.objects.filter(user=user_id).first()

            profile_edit_form = UserProfileForm(instance=authenticated_user_profile)

            return Response({'profile':user_profile, 'edit_form':profile_edit_form})
       

        

        
        return Response({'profile':user_profile})


# class UpdateProfile(generics.UpdateAPIView):
#     serializer_class = ProfileSerializer

    
#     def put(self, request, user):
#         print("Great")
#         if request.method == 'PUT':
#             form = UserProfileForm(data=request.PUT, instance = request.user)
#             if form.is_valid():
#                 form.save()

#                 return redirect('/')
        



        

  

