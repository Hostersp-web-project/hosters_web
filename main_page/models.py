from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Import the User model if not already imported
from django.db import models
from django.contrib.auth.models import AbstractUser



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(author=User.objects.get(username='your_username'))

class Account(models.Model):
    email_address = models.EmailField(unique=True)
    # Add other fields as needed

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    publish = models.DateTimeField(default=timezone.now)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email_address'], name='unique_email'),
        ]