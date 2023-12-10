from django import forms
from .models import UserProfile
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']  # 'user' 필드는 폼에서 제외

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'university': forms.TextInput(attrs={'class': 'form-control'}),
            'major': forms.TextInput(attrs={'class': 'form-control'}),
            'bedtime': forms.NumberInput(attrs={'class': 'form-control'}),
            'wake_up_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'time_of_move_in': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone_number_1': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number_2': forms.TextInput(attrs={'class': 'form-control'}),
        }
