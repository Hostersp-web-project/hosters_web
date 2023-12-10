from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import render, redirect
from surveys_app.forms import RoommatePreferencesForm
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Create your views here.
def hosters_main(request):
    return render(request, 'main_page/main.html')

def login(request):

    return render(request, 'main_page/login.html')

# @login_required
# def login(request):
#     # 현재 로그인한 사용자의 CustomUser 모델 인스턴스 가져오기
#     current_user = request.user
#     return render(request, 'main_page/login.html', {'current_user': current_user})

def join(request):
    return render(request, 'main_page/join.html')
def mypage(request):
    return render(request, 'main_page/my_page.html')


from django.shortcuts import render, redirect
from surveys_app.models import RoommatePreferences
from surveys_app.forms import RoommatePreferencesForm

'''def survey_view(request):
    # 사용자가 로그인한지 확인합니다.
    if not request.user.is_authenticated:
        # 사용자가 로그인하지 않은 경우를 처리합니다.
        return redirect('main_page/login.html')  # 'login'을 실제 로그인 URL로 바꿉니다.

    # 사용자가 이미 설문 조사 기호를 가지고 있는지 확인합니다.
    preferences, created = RoommatePreferences.objects.get_or_create(user=request.user)

    # 양식이 제출된 경우
    if request.method == 'POST':
        roomform = RoommatePreferencesForm(request.POST, instance=preferences)
        if roomform.is_valid():
            roomform.save()
            # 양식이 성공적으로 제출된 경우 리디렉션 또는 다른 작업을 수행합니다.
    else:
        roomform = RoommatePreferencesForm(instance=preferences)

    return render(request, 'main_page/survey.html', {'form': roomform})

'''
from django.shortcuts import render, redirect
from surveys_app.models import RoommatePreferences
from surveys_app.forms import RoommatePreferencesForm
from checklist_app.models import UserPreferences
from checklist_app.forms import PositiveCheckListForm

def survey_view(request):
    if not request.user.is_authenticated:
        return redirect('main_page/login.html')  # 로그인 URL로 리다이렉트

    # 기존 RoommatePreferences 모델 인스턴스를 가져오거나 생성합니다.
    roommate_preferences, created_rp = RoommatePreferences.objects.get_or_create(user=request.user)

    # 새로운 UserPreferences 모델 인스턴스를 가져오거나 생성합니다.
    user_preferences, created_up = UserPreferences.objects.get_or_create(member_id=request.user)

    if request.method == 'POST':
        roommate_form = RoommatePreferencesForm(request.POST, instance=roommate_preferences)
        checklist_form = PositiveCheckListForm(request.POST, instance=user_preferences)

        if roommate_form.is_valid() and checklist_form.is_valid():
            roommate_form.save()
            checklist_form.save()
            

    else:
        roommate_form = RoommatePreferencesForm(instance=roommate_preferences)
        checklist_form = PositiveCheckListForm(instance=user_preferences)

    return render(request, 'main_page/survey.html', {
        'roommate_form': roommate_form,
        'checklist_form': checklist_form
    })
