# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def index(request):
    template = 'index.html'
    return render(request, template)
   



def profile_homepage(request):
    template = 'homepage.html'
    return render(request, template)



# function to register/sign up a new user

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  #usercreationform is a django form to create a new user
        if form.is_valid():
            form.save() #creates the new user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username, password = password)
            login(request, user)
            return HttpResponseRedirect('profile')
    else:
        form = UserCreationForm()

    return render(request, 'index.html', {'form' : form })





