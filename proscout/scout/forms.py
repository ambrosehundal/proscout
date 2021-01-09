from django import forms
from django.forms import ModelForm
from scout.models import Profile


MMA_CHOICES = (
    ("1", "Boxing"),
    ("2", "Wrestling"),
    ("3", "Jujitsu"),
    ("4", "Kickboxing")

)

class UserProfileForm(ModelForm):

    disciplines = forms.MultipleChoiceField(choices=MMA_CHOICES)
    class Meta:
        model = Profile
        fields = ['age', 'height', 'weight', 'hometown', 'country', 'disciplines', 'headline', 'summary']
