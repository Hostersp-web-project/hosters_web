from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main_page.views import hosters_main, login, mypage, join

app_name = 'hosters'


urlpatterns = [
    path('main/', hosters_main, name='main'),
    path('login/', login, name='login'),
    path('join/', join, name='join'),
    path('mypage/', mypage, name='mypage'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)