from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.models import models

class RegisterForm(UserCreationForm):
    email = models.EmailField()
    
    class Meta:


