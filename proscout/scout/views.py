# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect


from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from scout.forms import UserProfileForm

from .models import Profile



import requests
import praw
# Create your views here.

# homepage
def index(request):
    template = 'index.html'
    return render(request, template)



# function for logged in user to create a new profile
def new_profile(request):
    current_user = request.user
    print(current_user)
    print("Balle")
    print(request.method)
    if request.method == "POST":	    
        form = UserProfileForm(request.POST)	        
        if form.is_valid():	        
            user_profile = Profile()	            
            user_profile.user = request.user	          
            user_profile.birth_date = form.cleaned_data['birth_date']	            
            user_profile.height = form.cleaned_data['height']
            user_profile.weight = form.cleaned_data['weight']
            user_profile.country = form.cleaned_data['country']
            user_profile.disciplines = form.cleaned_data['disciplines']
            user_profile.headline = form.cleaned_data['headline']
            user_profile.summary = form.cleaned_data['summary']
            user_profile.save()	            
            return redirect("/")
        else:
            print("Not valid")
            form = UserProfileForm()

    return render(request, "profile.html", {"form":form})




    
   


@login_required
def profile_homepage(request):

     
    create_profile_template = 'profile.html'

    profile_template = 'homepage.html'
    
    current_user = request.user

    #If User already has a profile, display profile instead of form
    if Profile.objects.filter(user=current_user).exists():
        user_profile = Profile.objects.get(user=current_user)
        print("profile exists")

        return render(request, profile_template, {'user': current_user, 'profile':user_profile})
    else:
        form = UserProfileForm()
  
    return render(request, create_profile_template, {'user': current_user, 'form': form})




def mma_subreddit():
    reddit = praw.Reddit(client_id='PERSONAL_USE_SCRIPT_14_CHARS', \
                     client_secret='SECRET_KEY_27_CHARS ', \
                     user_agent='YOUR_APP_NAME', \
                     username='YOUR_REDDIT_USER_NAME', \
                     password='YOUR_REDDIT_LOGIN_PASSWORD')         













