# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from scout.forms import UserProfileForm


# Create your views here.


def index(request):
    template = 'index.html'
    return render(request, template)
   



def profile_homepage(request):
    current_user = request.user
    form = UserProfileForm()
   
    template = 'homepage.html'
    return render(request, template, {'user': current_user, 'form': form})


def save_profile(request):
    current_user = request.user
    print(current_user)
    if response.method == "POST":
        form = UserProfileForm(response.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.profile_user = request.user
            user_profile.save()
            # user_profile = Profile()
            # user_profile.profile_user = current_user
            # user_profile.age = form.cleaned_data['age']
            # user_profile.height = form.cleaned_data['height']
            # user_profile.weight = form.cleaned_data['weight']
            # user_profile.country = form.cleaned_data['country']
            # user_profile.disciplines = form.cleaned_data['disciplines']
            # user_profile.headline = form.cleaned_data['headline']
            # user_profile.summary = form.cleaned_data['summary']
            # user_profile.save()
            return redirect("/index")
        else:
            form = UserProfileForm()
    
    return render(response, "index.html", {"form":form})


            













