from django import forms
from django.forms import ModelForm
from scout.models import Profile

class UserProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['age', 'height', 'weight', 'hometown', 'country', 'headline', 'summary']
