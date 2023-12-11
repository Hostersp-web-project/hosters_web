from django.shortcuts import render, redirect
from surveys_app.forms import RoommatePreferencesForm
from django.shortcuts import render
from datetime import datetime, timedelta
from collections import deque
import pymysql
import numpy as np
import pandas as pd
from django.contrib.auth.decorators import login_required
# Create your views here.


def hosters_main(request):
    if not request.user.is_authenticated:
        return redirect('hosters:login')   # 로그인 URL로 리다이렉트
    user_id = request.user.id

    conn = pymysql.connect(host ='db-k04ce-kr.vpc-pub-cdb.ntruss.com', user = 'alsrl', password = 'hosters123!', db = 'hosters-test', charset = 'utf8')

    sqlau = "SELECT * FROM auth_user"
    AU = pd.read_sql(sqlau, conn)
    
    sqlus = "SELECT * FROM UserScore"
    US = pd.read_sql(sqlus, conn)
    
    sqlpc = "SELECT * FROM Positive_Check_List"
    PC = pd.read_sql(sqlpc, conn)
    
    conn.close()
    if (user_id not in set(PC['member_id'])) or (user_id not in set(US['user_id'])) :
        return redirect('hosters:mypage')

    US = US.set_index('user_id')
    PC = PC.set_index('member_id')
        
    # S 가중치 계산함수
    def S_weight(user_id):
        X = US.at[user_id, 'head_score']*(20/100)
        return X

    def HAIR_Score(user1_id, user2_id):
        # 인덱스를 사용하여 HAIR 값을 검색합니다.
        user1_H1_score = US.at[user1_id, 'hair_score']
        user2_H1_score = US.at[user2_id, 'hair_score']

        # 기존의 계산을 그대로 사용합니다.
        x = user1_H1_score - 50
        y = user2_H1_score - 50
        H1 = np.abs(x - y)

        return H1

    def HEART_Score(user1_id, user2_id):
        user1_H1_score = US.at[user1_id, 'heart_score']
        user2_H1_score = US.at[user2_id, 'heart_score']
        x = user1_H1_score - 50
        y = user2_H1_score - 50
        H3 = np.abs(x-y)
        return H3

    def HAND_Score(user1_id, user2_id):
        user1_H1_score = US.at[user1_id, 'hand_score']
        user2_H1_score = US.at[user2_id, 'hand_score']
        x = user1_H1_score - 50
        y = user2_H1_score - 50
        H4 = np.abs(x-y)
        return H4

    def P_C_L_S(user1_id, user2_id):
        # 사용자 ID를 인덱스로 사용하여 두 사용자의 취미 데이터를 가져옵니다.
        user1_hobbies = PC.loc[user1_id]
        user2_hobbies = PC.loc[user2_id]

        # 1 값을 가지는 취미들의 집합을 구합니다.
        user1_hobbies_set = set(user1_hobbies[user1_hobbies == 1].index)
        user2_hobbies_set = set(user2_hobbies[user2_hobbies == 1].index)

        # 공통 취미활동 집합
        common_hobbies = user1_hobbies_set.intersection(user2_hobbies_set)

        # 합집합 취미활동 집합
        all_hobbies = user1_hobbies_set.union(user2_hobbies_set)

        # Jaccard 유사도 계산
        if not all_hobbies:  # 합집합이 비어있는 경우
            return 0
        jaccard_similarity = len(common_hobbies) / len(all_hobbies)

        return jaccard_similarity * 100  # 백분율로 반환


        
    def scoreCalc(user1_id, user2_id):
        A = 300 - (HAIR_Score(user1_id, user2_id) + HEART_Score(user1_id, user2_id) + HAND_Score(user1_id, user2_id))
        B = 75 + S_weight(user1_id)
        C = A * (B / 300)
        Rp = 100 - B
        D = C + P_C_L_S(user1_id, user2_id) * (Rp / 100)
        return D

    def get_user_queue(user1_id, AU, max_users=15):
        """
        현재 시간을 기준으로 과거 방향으로 시간을 확장해가며 사용자를 찾아 큐를 초기화하는 함수
        """
        current_time = datetime.now()
        time_delta = timedelta(hours=1)
        
        res = deque()
        removed_user={user1_id}

        while True:
            start_time = current_time - time_delta
            users_in_time_window = AU[(AU['last_login'] >= start_time) & (AU['last_login'] <= current_time)]
            score_list=[]
            user_queue = set()
            
            # 큐에 사용자 추가
            for new_user in users_in_time_window['id']:
                if not (new_user in removed_user):
                    user_queue.add(new_user)
            
            for i in user_queue:
                user2_id = i
                
                D = scoreCalc(user1_id, user2_id)
                score_list.append((user2_id, D))

            score_list.sort(key=lambda x: -x[1])

            for i in score_list:
                res.append(i)
                removed_user.add(i[0])
            # 큐가 가득 찼거나 데이터프레임의 시작 시간에 도달했으면 중단
            if len(res) >= max_users or start_time <= AU['last_login'].min():
                break

            # 시간 범위 확장
            current_time -= time_delta

        return res
    print(get_user_queue(user_id, AU))

    return render(request, 'main_page/main.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('hosters:main')
    return render(request, 'main_page/login.html')

def match(request):
    if not request.user.is_authenticated:
        return redirect('hosters:login')
    return render(request, 'main_page/match.html')
def mypage(request):
    if not request.user.is_authenticated:
        return redirect('hosters:login')
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
    
    conn = pymysql.connect(host ='db-k04ce-kr.vpc-pub-cdb.ntruss.com', user = 'alsrl', password = 'hosters123!', db = 'hosters-test', charset = 'utf8')

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
            #df2 = pd.DataFrame.from_records(up)
            df1 = df1.fillna(0).loc[0]
                        
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
            print(set(check["user_id"]))
            print(user_id)
            curs = conn.cursor()
            if user_id not in set(check["user_id"]) :
                update = 'INSERT INTO UserScore VALUES (%s, %s, %s, %s, %s, %s)'
                curs.execute(update, (user_id, HAIR, HEAD, HEART, HAND, res3(HAIR, HEART, HAND)))
            else:
                update = "UPDATE UserScore SET hair_score = %s, head_score = %s, heart_score = %s, hand_score = %s, result = %s WHERE user_id = %s;"
                curs.execute(update, (HAIR, HEAD, HEART, HAND, res3(HAIR, HEART, HAND), user_id))
            #update = 'INSERT INTO UserScore VALUES (%s, %s, %s, %s, %s, %s)'
            #update = "UPDATE UserScore SET hair_score = %s, head_score = %s, heart_score = %s, hand_score = %s, result = %s WHERE user_id = %s;"
            #curs.execute(update, (HAIR, HEAD, HEART, HAND, res3(HAIR, HEART, HAND), user_id))
            conn.commit()
            curs.close()
            conn.close()

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



