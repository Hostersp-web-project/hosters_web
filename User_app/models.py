

# Create your models here.
from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    gender = {
        ('남자', '남자'),
        ('여자', '여자')
    }
    accom = {
        ('기숙사', '기숙사'),
        ('아파트', '아파트'),
        ('빌라', '빌라'),
        ('오피스텔', '오피스텔')
    }

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=8, choices=gender, default='남자')
    age = models.IntegerField()
    university = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    bedtime = models.IntegerField()
    wake_up_time = models.IntegerField()
    time_of_move_in = models.IntegerField()
    form = models.CharField(max_length=5, choices=accom, default='기숙사')
    phone_number_1 = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    kakaotalk = models.CharField(max_length=255)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'User'