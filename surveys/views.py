from django.shortcuts import render, redirect
from .models import SurveyResult

def mypage_with_survey(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        question1 = request.POST.get('mbti_agree1')

        # SurveyResult 모델에 저장
        survey_result = SurveyResult(
            user_id=user_id,
            question1=question1,
            # 다른 질문에 대한 처리를 필요에 따라 추가
        )
        survey_result.save()

    return render(request, 'main_page/my_page.html')
