from django.shortcuts import render, redirect
from surveys_app.forms import RoommatePreferencesForm
from django.shortcuts import render
from datetime import datetime, timedelta
import pymysql
import numpy as np
import pandas as pd
from django.http import JsonResponse


# Create your views here.
global calculator
def increment(request):
    global calculator
    ind = request.session.get('ind', 0)
    ind += 1
    request.session['ind'] = ind
    # ScoreCalculator 클래스의 인스턴스 생성
    # 점수 계산 및 가져오기
    scores = calculator.get_scores(request.session.get('ind', 0))
    print({'ind': request.session.get('ind', 0), "score": scores[request.session.get('ind', 0)]})
    return JsonResponse({'ind': request.session.get('ind', 0), "score": scores[request.session.get('ind', 0)]})


def hosters_main(request):
    global calculator
    if not request.user.is_authenticated:
        return redirect('hosters:login')  # 로그인 URL로 리다이렉트
    calculator = ScoreCalculator(user_id=request.user.id)
    if 'ind' not in request.session:
        request.session['ind'] = 0

    # ScoreCalculator 클래스의 인스턴스 생성

    # ind 값을 세팅

    # 카드 설정
    calculator.set_cards()

    # 점수 계산 및 가져오기
    scores = calculator.get_scores(request.session.get('ind', 0))
    print(scores)
    # 데이터베이스 연결 종료
    #calculator.close_database_connection()

    return render(request, 'main_page/main.html', {"ind": request.session.get('ind', 0), "score": request.session.get('ind', 0)})


def login(request):
    if request.user.is_authenticated:
        return redirect('hosters:main')
    return render(request, 'main_page/login.html')

def match(request):
    if not request.user.is_authenticated:
        return redirect('hosters:login')
    return render(request, 'main_page/cards.html')
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


'''def find_mutual_likes(request):
    if not request.user.is_authenticated:
        return redirect('hosters:login')

    conn = pymysql.connect(host ='db-k04ce-kr.vpc-pub-cdb.ntruss.com', user = 'alsrl', password = 'hosters123!', db = 'hosters-test', charset = 'utf8')

    sqlau = "SELECT * FROM auth_user"
    Liked = pd.read_sql(sqlau, conn)
    user_id = request.user.id
    # 사용자가 '좋아요'를 누른 모든 사용자 찾기
    liked_users = Like.objects.filter(liker=user_id).values_list('liked', flat=True)

    # 상호적인 '좋아요'를 찾기
    mutual_likes = []
    for liked_user in liked_users:
        if Like.objects.filter(liker=liked_user, liked=user).exists():
            mutual_likes.append(liked_user)

    return mutual_likes

'''

class ScoreCalculator:
    def __init__(self, user_id):
        self.user_id = user_id
        self.cards = None
        self.AU = None
        self.US = None
        self.PC = None
        self.res = None
        self.user = None
        self.ids = None
    def set_cards(self):
        host = 'db-k04ce-kr.vpc-pub-cdb.ntruss.com'
        user = 'alsrl'
        password = 'hosters123!'
        db = 'hosters-test'
        charset = 'utf8'

        try:
            conn = pymysql.connect(host=host, user=user, password=password, db=db, charset=charset)
            print("Successfully connected to the database.")
        except pymysql.Error as e:
            print(f"Error connecting to the database: {e}")

        sqlau = "SELECT * FROM auth_user"
        sqlus = "SELECT * FROM UserScore"
        sqlpc = "SELECT * FROM Positive_Check_List"
        sqluser = "SELECT * FROM User"

        self.AU = pd.read_sql(sqlau, conn)
        self.US = pd.read_sql(sqlus, conn).set_index('user_id')
        self.PC = pd.read_sql(sqlpc, conn).set_index('member_id')
        self.res = pd.read_sql(sqlus, conn)[["user_id", "result"]]
        self.user = pd.read_sql(sqluser, conn)

        conn.close()
        print("Database connection closed.")

        cards = pd.concat(
            [self.res.merge(self.user, how='left', left_on='user_id', right_on='User_id'), self.AU["last_login"]],
            axis=1, join='inner')
        cards["datesort"] = cards["last_login"].dt.date
        cards["hoursort"] = cards["last_login"].dt.hour
        cards = cards.set_index("user_id").drop(labels=self.user_id, axis=0)
        cards = cards.sort_values(["datesort", "hoursort"], ascending=False)
        cards["score"] = np.nan
        self.ids = cards.index.values.tolist()
        print(self.ids)
        self.cards = cards.drop(labels="User_id", axis=1).fillna(0)
        return self.cards

    def S_weight(self, user_id):
        X = self.US.at[user_id, 'head_score']*(20/100)
        return X

    def HAIR_Score(self, user1_id, user2_id):
        user1_H1_score = self.US.at[user1_id, 'hair_score']
        user2_H1_score = self.US.at[user2_id, 'hair_score']
        x = user1_H1_score - 50
        y = user2_H1_score - 50
        H1 = np.abs(x - y)
        return H1

    def HEART_Score(self, user1_id, user2_id):
        user1_H1_score = self.US.at[user1_id, 'heart_score']
        user2_H1_score = self.US.at[user2_id, 'heart_score']
        x = user1_H1_score - 50
        y = user2_H1_score - 50
        H3 = np.abs(x - y)
        return H3

    def HAND_Score(self, user1_id, user2_id):
        user1_H1_score = self.US.at[user1_id, 'hand_score']
        user2_H1_score = self.US.at[user2_id, 'hand_score']
        x = user1_H1_score - 50
        y = user2_H1_score - 50
        H4 = np.abs(x - y)
        return H4

    def P_C_L_S(self, user1_id, user2_id):
        user1_hobbies = self.PC.loc[user1_id]
        user2_hobbies = self.PC.loc[user2_id]
        user1_hobbies_set = set(user1_hobbies[user1_hobbies == 1].index)
        user2_hobbies_set = set(user2_hobbies[user2_hobbies == 1].index)
        common_hobbies = user1_hobbies_set.intersection(user2_hobbies_set)
        all_hobbies = user1_hobbies_set.union(user2_hobbies_set)
        if not all_hobbies:
            return 0
        jaccard_similarity = len(common_hobbies) / len(all_hobbies)
        return jaccard_similarity * 100

    def scoreCalc(self, user1_id, user2_id):
        A = 300 - (self.HAIR_Score(user1_id, user2_id) + self.HEART_Score(user1_id, user2_id) + self.HAND_Score(
            user1_id, user2_id))
        B = 75 + self.S_weight(user1_id)
        C = A * (B / 300)
        Rp = 100 - B
        D = C + self.P_C_L_S(user1_id, user2_id) * (Rp / 100)
        return D

    def calculate_scores(self, ind):
        cards = self.cards
        print(len(cards.iloc[ind:].index))
        if len(cards.iloc[ind:].index) >= 15:
            for i in range(15):
                if cards.loc[self.ids[i + ind]]["score"] == 0:
                    cards.at[self.ids[i + ind], "score"] = self.scoreCalc(self.user_id, self.ids[i + ind])
            cards['datesort'] = pd.to_datetime(cards["datesort"])
            cards['hoursort'] = cards['hoursort'].astype(int)
            cards['score'] = cards['score'].astype(float)
            cards = cards.sort_values(by=["datesort", "hoursort", "score"], ascending=False)
        cards["score"] = cards["score"].round(1)
        return cards

    def get_scores(self, ind):
        cards = self.calculate_scores(ind)
        scores = cards.to_dict('records')
        return scores
