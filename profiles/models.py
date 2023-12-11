# profiles/models.py
from django.db import models
from django.contrib.auth.models import User

class Like(models.Model):
    liker = models.ForeignKey(User, related_name='liker', on_delete=models.CASCADE)
    liked = models.ForeignKey(User, related_name='liked', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('liker', 'liked')  # Ensure that each pair is unique
