from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from surveys_app.forms import RoommatePreferencesForm
from django.shortcuts import render
import numpy as np
import pandas as pd
from django.contrib.auth.decorators import login_required
import pymysql
# Create your views here.
conn = pymysql.connect(host ='db-k04ce-kr.vpc-pub-cdb.ntruss.com', user = 'alsrl', password = 'hosters123!', db = 'hosters-test', charset = 'utf8')


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
from checklist_app.models import UserPreferences
from checklist_app.forms import PositiveCheckListForm
from User_app.forms import UserProfileForm
from User_app.models import UserProfile
def survey_view(request):
    if not request.user.is_authenticated:
        return redirect('main_page/login.html')  # 로그인 URL로 리다이렉트
    user_id = request.user.id

    # 기존 RoommatePreferences 모델 인스턴스를 가져오거나 생성합니다.
    roommate_preferences, created_rp = RoommatePreferences.objects.get_or_create(user=request.user)
    
    # 새로운 UserPreferences 모델 인스턴스를 가져오거나 생성합니다.
    user_preferences, created_up = UserPreferences.objects.get_or_create(member_id=request.user)
    in_preferences, created_in = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        roommate_form = RoommatePreferencesForm(request.POST, instance=roommate_preferences)
        checklist_form = PositiveCheckListForm(request.POST, instance=user_preferences)
        user_form = UserProfileForm(request.POST, instance=in_preferences)

        if roommate_form.is_valid() and checklist_form.is_valid()and user_form.is_valid():
            roommate_form.save()
            checklist_form.save()
            user_form.save()

            sql = 'SELECT * FROM roommate_preferences WHERE user_id = '+ str(user_id)

            # DataFrame 변환
            df1 = pd.read_sql(sql, conn)
            print(df1)
            #df2 = pd.DataFrame.from_records(up)
            df1 = df1.fillna(0).loc[0]
            print(df1)
                        
            # HAIR_1 변수를 사용하여 N_H1 정의
            HAIR_1 = ["clean_bathroom_periodically",
                    "clean_dust_immediately",
                    "vacuum_once_a_day",
                    "clean_hair_dust_immediately"]
            N_H1 = df1[HAIR_1]

            HAIR_2 = ["tidiness_waste_energy",
                    "tidiness_not_needed",
                    "Cleaning_Non_Priority_Daily_Life"] # Don't you put cleaning as a priority in your daily life?
            N_H2 = df1[HAIR_2]

            HEAD_S = ["roommate_pet_ok", "no_friends_without_permission", "roommate_drink_less", 'Daily_Life_Stress_Susceptibility']
            N_S = df1[HEAD_S]

            HEAD_F = ["late_night_calls_ok",
            "long_bathroom_use_ok",
            "clothes_borrowing_ok",
            "enter_without_knocking_ok"]
            N_F = df1[HEAD_F]

            HEART_C = ["roommate_pet_ok",
            "meals_with_roommate_important",
            "roommate_drink_alcohol_well",
            "emotional_closeness_good",
            "movie_watching_times",
            "age_difference_ok"]
            N_C = df1[HEART_C]

            HEART_D = ["same_hobbies_not_needed",
            "maintain_some_distance", "Different_Hobbies_Relationship_Impact"]
            N_D = df1[HEART_D]

            HAND_I = ["not_clean_others_mess", "Self_Responsibility_in_Household_Chores_Effectiveness", "Individual_Family_Member_Household_Chores_Responsibility"]
            N_I = df1[HAND_I]
            HAND_T = ["share_household_chores", "Housework_Family_Roles_Over_Individual_Tasks"]
            N_T = df1[HAND_T]

            # 나머지 변수들도 위와 같은 방식으로 정의
            # HAIR, HEAD, HEART, HAND 점수 계산
            HAIR = (np.sum(N_H1) - np.sum(N_H2))/(len(N_H1)+len(N_H2))*25+50
            HEAD = (np.sum(N_S) - np.sum(N_F))/(len(N_S)+len(N_F))*25+50
            HEART = (np.sum(N_C) - np.sum(N_D))/(len(N_C)+len(N_D))*25+50
            HAND = (np.sum(N_I) - np.sum(N_T))/(len(N_I)+len(N_T))*25+50
            # 필요한 경우 HEART 값을 조정

            print(HAIR)
            
            sqlcheck = 'SELECT user_id FROM UserScore'
            check = pd.read_sql(sqlcheck, conn)
            curs = conn.cursor()
            if user_id not in check :
                update = 'INSERT INTO UserScore VALUES (%s, %s, %s, %s, %s, %s)'
            else:
                update = "UPDATE UserScore SET hair_score = %s, head_score = %s, heart_score = %s, hand_score = %s, result = %s WHERE user_id = %s;"
                curs.execute(update, (HAIR, HEAD, HEART, HAND, res3(HAIR, HEART, HAND), user_id))
            #update = 'INSERT INTO UserScore VALUES (%s, %s, %s, %s, %s, %s)'
            #update = "UPDATE UserScore SET hair_score = %s, head_score = %s, heart_score = %s, hand_score = %s, result = %s WHERE user_id = %s;"
            #curs.execute(update, (HAIR, HEAD, HEART, HAND, res3(HAIR, HEART, HAND), user_id))
            conn.commit()
            curs.close()

    else:
        roommate_form = RoommatePreferencesForm(instance=roommate_preferences)
        checklist_form = PositiveCheckListForm(instance=user_preferences)
        user_form = UserProfileForm(instance=in_preferences)

    return render(request, 'main_page/my_page.html', {
        'roommate_form': roommate_form,
        'checklist_form': checklist_form,
        'user_form': user_form
    })



def res3(hair, heart, hand):
    if hair > 50:
        h = "H1"
    else:
        h = "H2"
    if heart > 50:
        s = "C"
    else:
        s = "D"
    if hand > 50:
        t = "T"
    else:
        t = "I"
    return h + s + t



