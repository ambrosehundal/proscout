from django import forms
from django.forms import ModelForm
from scout.models import Profile


MMA_CHOICES = (
    ("1", "Boxing"),
    ("2", "Wrestling"),
    ("3", "Brazilian Jujitsu"),
    ("4", "Kickboxing"),
    ("5", "Judo"),
    ("6", "Muay Thai"),
)

MMA_EXPERIENCE_LEVEL = (
    ("1", "Amateur"),
    ("2", "Professional")

)


MMA_ROLE = (
    ("1", "Fighter"),
    ("2", "Coach"),
    ("3", "Both"),

)

class UserProfileForm(forms.ModelForm):

    disciplines = forms.MultipleChoiceField(choices=MMA_CHOICES, widget=forms.CheckboxSelectMultiple)
    mma_experience_level = forms.MultipleChoiceField(choices=MMA_EXPERIENCE_LEVEL)
    role = forms.MultipleChoiceField(choices=MMA_ROLE)
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'birth_date', 'height', 'weight', 'weight_units', 'hometown', 'country', 'disciplines', 'mma_experience_level', 'headline', 'summary', 'image', 'role']
