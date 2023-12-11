# profiles/admin.py

from django.contrib import admin
from .models import Profile, Like

admin.site.register(Profile)
admin.site.register(Like)
