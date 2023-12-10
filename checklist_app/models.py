from django.db import models
from django.conf import settings


from django.db import models
from django.conf import settings

class UserPreferences(models.Model):
    # 선택지 정의
    
    member = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    sports = models.BooleanField(default=False)
    music = models.BooleanField(default=False)
    arts_crafts = models.BooleanField(default=False)
    reading = models.BooleanField(default=False)
    cooking = models.BooleanField(default=False)
    movies_tv = models.BooleanField(default=False)
    gaming = models.BooleanField(default=False)
    traveling = models.BooleanField(default=False)
    language_learning = models.BooleanField(default=False)
    outdoor_activities = models.BooleanField(default=False)
    fitness = models.BooleanField(default=False)
    technology = models.BooleanField(default=False)
    social_activities = models.BooleanField(default=False)
    meditation = models.BooleanField(default=False)
    pet_care = models.BooleanField(default=False)
    # ... 나머지 필드들

    class Meta:
        db_table = 'Positive_Check_List'



'''class User(models.Model):
    name = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)

    def __str__(self):
        return self.name
'''