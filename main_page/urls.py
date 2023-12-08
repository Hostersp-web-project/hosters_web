from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main_page.views import hosters_main, login, mypage, join, survey_view


app_name = 'hosters'


urlpatterns = [
    path('main/', hosters_main, name='main'),
    path('login/', login, name='login'),
    path('join/', join, name='join'),
    path('mypage/', mypage, name='mypage'),
    path('survey/', survey_view, name='survey'),
    # 다른 URL 패턴들을 필요에 따라 추가
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)