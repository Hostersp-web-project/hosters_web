from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login
from .models import RoommatePreferences

# def google_login(request):
#     # Google API로부터 받은 정보를 처리하는 코드
#     # 예를 들어, request에서 Google user_id를 추출하는 로직
#     google_user_id = get_google_user_id_from_request(request)
#
#     # Django의 User 모델과 연결
#     user = authenticate_google_user(google_user_id)
#
#     # 이 사용자에 대한 RoommatePreferences 객체가 있는지 확인하고, 없으면 생성
#     preferences, created = RoommatePreferences.objects.get_or_create(user=user)
#
#     # 필요한 경우 여기서 preferences 객체를 업데이트
#     # preferences.some_field = 'some_value'
#     # preferences.save()
#
#     # 사용자를 로그인 시키기
#     login(request, user)
#
#     # 최종적으로 사용자를 리디렉션 시키기
#     return redirect('some_page')
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RoommatePreferencesForm
from .models import RoommatePreferences

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import RoommatePreferences
from .forms import RoommatePreferencesForm


@login_required
def create_roommate_preference(request):
    # Pass the user's ID to the template
    user_id = request.user.id

    if request.method == 'POST':
        form = RoommatePreferencesForm(request.POST)
        if form.is_valid():
            roommate_preference = form.save(commit=False)
            roommate_preference.user = request.user  # Set the logged-in user
            roommate_preference.save()
            return redirect('some_success_url')
    else:
        form = RoommatePreferencesForm()

    return render(request, 'roommate_preferences_form.html', {
        'form': form,
        'user_id': user_id  # Pass the user ID into the context for the template
    })