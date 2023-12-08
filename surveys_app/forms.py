from django import forms
from .models import RoommatePreferences

class RoommatePreferencesForm(forms.ModelForm):
    class Meta:
        exclude = ['user_id']
        model = RoommatePreferences
        # Include all fields or specify the fields you want


