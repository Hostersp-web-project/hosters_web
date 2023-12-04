from django.db import models

class SurveyResult(models.Model):
    user_id = models.CharField(max_length=255)
    question1 = models.CharField(max_length=50)
    # 다른 질문에 대한 필드들을 필요에 따라 추가

    def __str__(self):
        return f'{self.user_id} - Survey Result'

    class Meta:
        app_label = 'surveys'
