# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from scout.models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_filter = ['user']
    list_display = ['user']
    search_fields = ['user']
    readonly_fields = ['user']

    class Meta:
        model = Profile 


admin.site.register(Profile, ProfileAdmin)
