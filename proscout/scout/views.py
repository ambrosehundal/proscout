# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def index(request):
    template = 'index.html'
    return render(request, template)
   



def profile_homepage(request):
    template = 'homepage.html'
    return render(request, template)





