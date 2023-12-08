from django import forms
from .models import RoommatePreferences

from django import forms
from .models import RoommatePreferences

class RoommatePreferencesForm(forms.ModelForm):
    class Meta:
        exclude = ['user']
        model = RoommatePreferences
        # 다른 필드들을 포함하거나 원하는 필드를 지정합니다.
