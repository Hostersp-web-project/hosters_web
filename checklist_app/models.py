from django.db import models
from django.conf import settings


class UserPreferences(models.Model):
    CLEANING_CHOICES = [
        (1, 'Agree'),
        (0, 'Neutral'),
    ]

    member_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    sports = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    music = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    arts_crafts = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    reading = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    cooking = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    movies_tv = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    gaming = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    traveling = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    language_learning = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    outdoor_activities = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    fitness = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    technology = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    social_activities = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    meditation = models.IntegerField(choices=CLEANING_CHOICES, default=0)
    pet_care = models.IntegerField(choices=CLEANING_CHOICES, default=0)

    # Add other fields as needed

    class Meta:
        db_table = 'Positive_Check_List'


class User(models.Model):
    name = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)

    def __str__(self):
        return self.name