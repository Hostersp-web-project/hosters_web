from django.urls import path
from .views import mypage_with_survey
from django.conf.urls.static import static
from django.conf import settings
app_name = 'surveys'

urlpatterns = [
    path('mypage/', mypage_with_survey, name='mypage_with_survey'),
    # 다른 설문조사와 관련된 URL 패턴들을 필요에 따라 추가
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
