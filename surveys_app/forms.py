from django import forms
from .models import RoommatePreferences

class RoommatePreferencesForm(forms.ModelForm):
    class Meta:
        exclude = ['user']
        model = RoommatePreferences
        widgets = {
            'clean_bathroom_periodically': forms.RadioSelect(attrs={'class': 'clean-bathroom'}),
            'clean_dust_immediately': forms.RadioSelect(attrs={'class': 'clean-dust'}),
            'vacuum_once_a_day': forms.RadioSelect(attrs={'class': 'vacuum'}),
            'clean_hair_dust_immediately': forms.RadioSelect(attrs={'class': 'clean-hair-dust'}),
            'tidiness_waste_energy': forms.RadioSelect(attrs={'class': 'tidiness-waste'}),
            'tidiness_not_needed': forms.RadioSelect(attrs={'class': 'tidiness-not-needed'}),
            'Cleaning_Non_Priority_Daily_Life': forms.RadioSelect(attrs={'class': 'cleaning-non-priority'}),
            'roommate_pet_ok': forms.RadioSelect(attrs={'class': 'roommate-pet'}),
            'no_friends_without_permission': forms.RadioSelect(attrs={'class': 'no-friends'}),
            'roommate_drink_less': forms.RadioSelect(attrs={'class': 'roommate-drink-less'}),
            'Daily_Life_Stress_Susceptibility': forms.RadioSelect(attrs={'class': 'daily-life-stress'}),
            'late_night_calls_ok': forms.RadioSelect(attrs={'class': 'late-night-calls'}),
            'long_bathroom_use_ok': forms.RadioSelect(attrs={'class': 'long-bathroom-use'}),
            'clothes_borrowing_ok': forms.RadioSelect(attrs={'class': 'clothes-borrowing'}),
            'enter_without_knocking_ok': forms.RadioSelect(attrs={'class': 'enter-without-knocking'}),
            'meals_with_roommate_important': forms.RadioSelect(attrs={'class': 'meals-with-roommate'}),
            'roommate_drink_alcohol_well': forms.RadioSelect(attrs={'class': 'roommate-drink-well'}),
            'emotional_closeness_good': forms.RadioSelect(attrs={'class': 'emotional-closeness'}),
            'movie_watching_times': forms.RadioSelect(attrs={'class': 'movie-watching'}),
            'age_difference_ok': forms.RadioSelect(attrs={'class': 'age-difference'}),
            'same_hobbies_not_needed': forms.RadioSelect(attrs={'class': 'same-hobbies-not-needed'}),
            'maintain_some_distance': forms.RadioSelect(attrs={'class': 'maintain-distance'}),
            'Different_Hobbies_Relationship_Impact': forms.RadioSelect(attrs={'class': 'different-hobbies-impact'}),
            'not_clean_others_mess': forms.RadioSelect(attrs={'class': 'not-clean-others-mess'}),
            'Self_Responsibility_in_Household_Chores_Effectiveness': forms.RadioSelect(attrs={'class': 'self-responsibility'}),
            'Individual_Family_Member_Household_Chores_Responsibility': forms.RadioSelect(attrs={'class': 'family-member-responsibility'}),
            'share_household_chores': forms.RadioSelect(attrs={'class': 'share-chores'}),
            'Housework_Family_Roles_Over_Individual_Tasks': forms.RadioSelect(attrs={'class': 'family-roles'}),
        }

        # 다른 필드들을 포함하거나 원하는 필드를 지정합니다.
