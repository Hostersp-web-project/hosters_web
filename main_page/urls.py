from django.urls import path
from django.conf import settings
from django.conf.urls.static import static  
from main_page.views import hosters_main, login, match, survey_view, increment


app_name = 'hosters'


urlpatterns = [
    path('main/', hosters_main, name='main'),
    path('login/', login, name='login'),
    path('match/', match, name='match'),
    path('mypage/', survey_view, name='mypage'),
    
    path('increment/', increment, name='increment')
    # 다른 URL 패턴들을 필요에 따라 추가
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)