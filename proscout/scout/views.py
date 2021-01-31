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



def mma_subreddit(request):
    mma_news_template = 'mma_news.html'
    

    mma_subreddit = reddit.subreddit("mma").hot(limit=15)

    subreddit_results = []

    for post in mma_subreddit:
       
        subreddit_results.append(post)


    return render(request, mma_news_template, {'posts': subreddit_results} )

    
        


    


 


    

   
    













