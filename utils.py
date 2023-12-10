import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from collections import deque
'''
def initialize_user_queue(df, max_users=15):
    """
    현재 시간을 기준으로 과거 방향으로 시간을 확장해가며 사용자를 찾아 큐를 초기화하는 함수
    """
    current_time = datetime.now()
    time_delta = timedelta(hours=1)
    user_queue = deque()

    while len(user_queue) < max_users:
        start_time = current_time - time_delta
        users_in_time_window = df[(df['last_login'] >= start_time) & (df['last_login'] <= current_time)]

        # 큐에 사용자 추가
        for new_user in users_in_time_window['id']:
            if new_user not in user_queue:
                user_queue.append(new_user)
                if len(user_queue) >= max_users:
                    break

        # 큐가 가득 찼거나 데이터프레임의 시작 시간에 도달했으면 중단
        if len(user_queue) >= max_users or start_time <= df['last_login'].min():
            break

        # 시간 범위 확장
        time_delta += timedelta(hours=1)

    return user_queue

# 큐 업데이트 함수 재정의
def update_user_queue(user_queue, df, max_users=15):
    """
    사용자 선택에 따라 큐를 업데이트하는 함수
    """
    if user_queue:
        # 큐에서 첫 번째 사용자 제거 (가상의 사용자 선택)
        removed_user = user_queue.popleft()

        # 필요한 경우, 새로운 사용자 추가
        current_time = datetime.now()
        time_delta = timedelta(hours=1)

        while len(user_queue) < max_users:
            start_time = current_time - time_delta
            users_in_time_window = df[(df['last_login'] >= start_time) & (df['last_login'] <= current_time)]

            for new_user in users_in_time_window['id']:
                if new_user not in user_queue and new_user != removed_user:
                    user_queue.append(new_user)
                    if len(user_queue) >= max_users:
                        break

            # 큐가 가득 찼거나 데이터프레임의 시작 시간에 도달했으면 중단
            if len(user_queue) >= max_users or start_time <= df['last_login'].min():
                break

            # 시간 범위 확장
            time_delta += timedelta(hours=1)

    return user_queue




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
Hobby_list = df2.drop('member_id', axis=1).values.tolist()
Hobby_list

df2.set_index('member_id', inplace=True)

# 기존 데이터프레임 df에서 'id' 열만 선택하여 새 데이터프레임을 생성합니다.
ID = df1[['user_id']]
#ID = df[['id']]'''

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
'''

HAIR = (np.sum(N_H1, axis = 1) - np.sum(N_H2, axis = 1))/(N_S.shape[1]+N_F.shape[1])*25+50
HEAD = (np.sum(N_S, axis = 1) - np.sum(N_F, axis = 1))/(N_S.shape[1]+N_F.shape[1])*25+50
HEART = (np.sum(N_C, axis = 1) - np.sum(N_D, axis = 1))/(N_C.shape[1]+N_D.shape[1])*25+50
HAND = (np.sum(N_I, axis = 1) - np.sum(N_T, axis = 1))/(N_I.shape[1]+N_T.shape[1])*25+50
HEART.where(HEART < 50).dropna()
HAIR = HAIR.to_frame(name = "HAIR")
HEAD = HEAD.to_frame(name = "HEAD")
HEART = HEART.to_frame(name = "HEART")
HAND = HAND.to_frame(name = "HAND")

TH = ID.join(HAIR).join(HEAD).join(HEART).join(HAND)
TH["RES"] = TH.apply(lambda x : res3(x["HAIR"], x["HEART"], x["HAND"]), axis = 1)
TH.set_index('user_id', inplace=True)

HAIR_List = TH['HAIR'].tolist()
HAIR_List


HEAD_List = TH['HEAD'].tolist()

HEART_List = TH['HEART'].tolist()

HAND_List = TH['HAND'].tolist()

# S 가중치 계산함수
def S_weight(user_id):
    X = TH.at[user_id, 'HEAD']*(20/100)
    return X

# 두 유저 간의 HAIR_Score 차이
#def HAIR_Score(user1_id, user2_id):
#    user1_H1_score = HAIR_List[user1_id]
#    user2_H1_score = HAIR_List[user2_id]
#    x = user1_H1_score - 50
#    y = user2_H1_score - 50
#    H1 = np.abs(x-y)
#    return H1

def HAIR_Score(user1_id, user2_id):
    # 인덱스를 사용하여 HAIR 값을 검색합니다.
    user1_H1_score = TH.at[user1_id, 'HAIR']
    user2_H1_score = TH.at[user2_id, 'HAIR']

    # 기존의 계산을 그대로 사용합니다.
    x = user1_H1_score - 50
    y = user2_H1_score - 50
    H1 = np.abs(x - y)

    return H1

def HEART_Score(user1_id, user2_id):
    user1_H1_score = TH.at[user1_id, 'HEAD']
    user2_H1_score = TH.at[user2_id, 'HEAD']
    x = user1_H1_score - 50
    y = user2_H1_score - 50
    H3 = np.abs(x-y)
    return H3

def HAND_Score(user1_id, user2_id):
    user1_H1_score = TH.at[user1_id, 'HAND']
    user2_H1_score = TH.at[user2_id, 'HAND']
    x = user1_H1_score - 50
    y = user2_H1_score - 50
    H4 = np.abs(x-y)
    return H4


def P_C_L_S(user1_id, user2_id):
    # 사용자 ID를 인덱스로 사용하여 두 사용자의 취미 데이터를 가져옵니다.
    user1_hobbies = df2.loc[user1_id]
    user2_hobbies = df2.loc[user2_id]

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


def Matching_Score(user1_id):
    score_list = []
    user_queue = initialize_user_queue(df)
    while len(user_queue) < 15:
        for i in range(len(user_queue)):
            user2_id = user_queue[i]
            A = 300 - (HAIR_Score(user1_id, user2_id)+HEART_Score(user1_id, user2_id)+HAND_Score(user1_id, user2_id))
            B = 75 + S_weight(user1_id)
            C = A*(B/300)
            Rp = 100 - B
            D = C + P_C_L_S(user1_id, user2_id)*(Rp/100)
        score_list.append((user2_id, D))
        score_list.sort(key = lambda x : -x[1])
        if len(score_list) < 15:
            user_queue = update_user_queue(user_queue, df)       
    return score_list

'''