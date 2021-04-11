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
    form = UserProfileForm()
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




    
   


# @login_required
def profile_homepage(request, username):

    
    # create_profile_template = 'profile.html'

    profile_template = 'homepage.html'
    
    print("YES")

    #If User already has a profile, display profile instead of form
    if Profile.objects.filter(user=username).exists():
        user_profile = Profile.objects.get(user=username)
        print("profile exists")

        return render(request, profile_template, {'profile':user_profile})
    
    return redirect("/profile/create")
  
    


def update_profile(request):

    if request.method == 'POST':
        form = UserProfileForm(data=request.POST)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user)
            profile_form = UserProfileForm(request.POST, instance=profile)
            profile_form.save()
        
            return redirect('/home/profile/str:request.user')
        else:
            return redirect('/')


















def mma_subreddit(request):
    mma_news_template = 'mma_news.html'
    reddit = praw.Reddit(client_id='', \
                     client_secret='', \
                     user_agent='mma', \
                    )  

    mma_subreddit = reddit.subreddit("mma").hot(limit=15)

    subreddit_results = []

    for post in mma_subreddit:
       
        subreddit_results.append(post)


    return render(request, mma_news_template, {'posts': subreddit_results} )


def ufc_subreddit(request):
    ufc_posts_template = 'ufc_news.html'
    reddit = praw.Reddit(client_id='', \
                     client_secret='', \
                     user_agent='mma', \
                    )  

    ufc_subreddit = reddit.subreddit("ufc").hot(limit=25)

    subreddit_results = []

    for post in ufc_subreddit:
       
        subreddit_results.append(post)


    return render(request, ufc_posts_template, {'posts': subreddit_results} )



    
        


    


 


    

   
    













