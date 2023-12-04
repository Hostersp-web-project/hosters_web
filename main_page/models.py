from django.db import models

class Account(models.Model):
    EmailAddress = models.EmailField(unique=True)  # 예제 필드, 실제 필드로 대체

    # 다른 필드들

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['EmailAddress'], name='unique_email'),
]