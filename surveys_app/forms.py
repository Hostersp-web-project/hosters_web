from django import forms
from .models import RoommatePreferences

class RoommatePreferencesForm(forms.ModelForm):
    class Meta:
        exclude = ['user']
        model = RoommatePreferences
        widgets = {
            'clean_bathroom_periodically': forms.RadioSelect(attrs={'class': 'radio'}),
            'clean_dust_immediately': forms.RadioSelect(attrs={'class': 'radio'}),
            'vacuum_once_a_day': forms.RadioSelect(attrs={'class': 'radio'}),
            'clean_hair_dust_immediately': forms.RadioSelect(attrs={'class': 'radio'}),
            'tidiness_waste_energy': forms.RadioSelect(attrs={'class': 'radio'}),
            'tidiness_not_needed': forms.RadioSelect(attrs={'class': 'radio'}),
            'Cleaning_Non_Priority_Daily_Life': forms.RadioSelect(attrs={'class': 'radio'}),
            'roommate_pet_ok': forms.RadioSelect(attrs={'class': 'radio'}),
            'no_friends_without_permission': forms.RadioSelect(attrs={'class': 'radio'}),
            'roommate_drink_less': forms.RadioSelect(attrs={'class': 'radio'}),
            'Daily_Life_Stress_Susceptibility': forms.RadioSelect(attrs={'class': 'radio'}),
            'late_night_calls_ok': forms.RadioSelect(attrs={'class': 'radio'}),
            'long_bathroom_use_ok': forms.RadioSelect(attrs={'class': 'radio'}),
            'clothes_borrowing_ok': forms.RadioSelect(attrs={'class': 'radio'}),
            'enter_without_knocking_ok': forms.RadioSelect(attrs={'class': 'radio'}),
            'meals_with_roommate_important': forms.RadioSelect(attrs={'class': 'radio'}),
            'roommate_drink_alcohol_well': forms.RadioSelect(attrs={'class': 'radio'}),
            'emotional_closeness_good': forms.RadioSelect(attrs={'class': 'radio'}),
            'movie_watching_times': forms.RadioSelect(attrs={'class': 'radio'}),
            'age_difference_ok': forms.RadioSelect(attrs={'class': 'radio'}),
            'same_hobbies_not_needed': forms.RadioSelect(attrs={'class': 'radio'}),
            'maintain_some_distance': forms.RadioSelect(attrs={'class': 'radio'}),
            'Different_Hobbies_Relationship_Impact': forms.RadioSelect(attrs={'class': 'radio'}),
            'not_clean_others_mess': forms.RadioSelect(attrs={'class': 'radio'}),
            'Self_Responsibility_in_Household_Chores_Effectiveness': forms.RadioSelect(attrs={'class': 'radio'}),
            'Individual_Family_Member_Household_Chores_Responsibility': forms.RadioSelect(attrs={'class': 'radio'}),
            'share_household_chores': forms.RadioSelect(attrs={'class': 'radio'}),
            'Housework_Family_Roles_Over_Individual_Tasks': forms.RadioSelect(attrs={'class': 'radio'}),
            'drinks_alcohol' : forms.RadioSelect(attrs={'class': 'radio'}),
            'smokes_cigarettes' : forms.RadioSelect(attrs={'class': 'radio'}),
            'smokes_indoors' : forms.RadioSelect(attrs={'class': 'radio'})
    

        }

        # 다른 필드들을 포함하거나 원하는 필드를 지정합니다.
