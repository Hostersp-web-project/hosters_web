from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import RoommatePreferences, User

admin.site.register(RoommatePreferences)
admin.site.register(User)