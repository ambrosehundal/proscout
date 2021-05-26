# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.






class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField()
    height = models.IntegerField(default = 72)
    weight = models.IntegerField(default = 180)
    weight_units = models.CharField(max_length=30, blank=False, default='pounds')
    hometown = models.CharField(max_length=40, blank=True)
    country = models.CharField(max_length=30, null=True)
    disciplines = models.CharField(max_length=255, blank=True) # martial art disciplines
    mma_experience_level = models.CharField(max_length=50, blank=True)
    wins = models.IntegerField(default=0, blank=True)
    losses = models.IntegerField(default=0, blank=True)
    draws = models.IntegerField(default=0, blank=True)
    headline = models.CharField(max_length=150, blank=True)
    summary = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)
    role = models.CharField(max_length=255, null=True)
    

    def __str__(self):
        return self.headline
    
# class Experience(models.Model)





