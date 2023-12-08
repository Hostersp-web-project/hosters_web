from django.db import models
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(author_id='user_id')



class Account(models.Model):
    EmailAddress = models.EmailField(unique=True)  # 예제 필드, 실제 필드로 대체
    objects = models.Manager()
    published = PublishedManager()

    # 다른 필드들

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    publish = models.DateTimeField(default=timezone.now)


    class Mata:
        constraints = [
            models.UniqueConstraint(fields=['EmailAddress'], name='unique_email'),
]


