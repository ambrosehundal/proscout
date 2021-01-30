# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.






class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=50, default="Conor")
    last_name = models.CharField(max_length=50, default="Mcgregor")
    birth_date = models.DateField()
    height = models.IntegerField(default = 72)
    weight = models.IntegerField(default = 180)
    hometown = models.CharField(max_length=40, blank=True)
    country = models.CharField(max_length=30, null=True)
    disciplines = models.CharField(max_length=255, blank=True) # martial art disciplines
    headline = models.CharField(max_length=150, blank=True)
    summary = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)
    






