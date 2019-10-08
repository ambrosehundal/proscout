# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Athlete(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default = 1)
    birth_date = models.CharField(max_length=20)
    hometown = models.CharField(max_length=40)
    country = models.CharField(max_length=30)
    primary_sport = models.CharField(max_length=20)



