from django.urls import path
from django.conf import settings
from django.conf.urls.static import static  
from main_page.views import hosters_main, login, matched, survey_view


app_name = 'hosters'


urlpatterns = [
    path('main/', hosters_main, name='main'),
    path('login/', login, name='login'),
    path('matched/', matched, name='matched'),
    path('mypage/', survey_view, name='mypage')
    
    # 다른 URL 패턴들을 필요에 따라 추가
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)