from django.contrib import admin
from . import models

class profiles(admin.ModelAdmin):
    list_display = ('name','email','dob', 'bio', 'photo')
    pass


admin.site.register(models.UserProfile, profiles)