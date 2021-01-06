# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Athlete(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     age = models.IntegerField(default = 1)
#     birth_date = models.CharField(max_length=20)
#     hometown = models.CharField(max_length=40)
#     country = models.CharField(max_length=30)
    




class Profile(models.Model):
    profile_user = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
    age = models.IntegerField(default = 1)
    # birth_date = models.CharField(max_length=20)
    height = models.IntegerField(default = 72)
    weight = models.IntegerField(default = 180)
    hometown = models.CharField(max_length=40, blank=True)
    country = models.CharField(max_length=30, null=True)
    headline = models.CharField(max_length=150, blank=True)
    summary = models.CharField(max_length=200, blank=True)



