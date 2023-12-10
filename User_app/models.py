from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    university = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    bedtime = models.IntegerField()
    wake_up_time = models.IntegerField()
    time_of_move_in = models.IntegerField()
    phone_number_1 = models.CharField(max_length=255)
    phone_number_2 = models.CharField(max_length=255)

    def __str__(self):
        return self.name
