from django import forms
from .models import UserPreferences


class PositiveCheckListForm(forms.ModelForm):
    class Meta:
        exclude = ['member']
        model = UserPreferences
        fields = ['sports', 'music', 'arts_crafts', 'reading', 'cooking', 'movies_tv',  
        'gaming' , 'traveling',  'language_learning', 'outdoor_activities',
         'fitness', 'technology',  'social_activities', 'meditation', 'pet_care']