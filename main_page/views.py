from django.shortcuts import render, redirect
from django.utils import timezone


# Create your views here.
def hosters_main(request):
    return render(request, 'main_page/main.html')

def login(request):
    return render(request, 'main_page/login.html')

def join(request):
    return render(request, 'main_page/join.html')
def mypage(request):
    return render(request, 'main_page/my_page.html')

