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
    current_user = request.user
    print(current_user)
    template = 'homepage.html'
    return render(request, template, {'user': current_user})









