from django import forms
from .models import UserProfile
class UserProfileForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = " "
    class Meta:
        model = UserProfile
        exclude = ['user']  # 'user' 필드는 폼에서 제외

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control-name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control-time'}),
            'university': forms.TextInput(attrs={'class': 'form-control-uni'}),
            'major': forms.TextInput(attrs={'class': 'form-control-uni'}),
            'bedtime': forms.NumberInput(attrs={'class': 'form-control-time'}),
            'wake_up_time': forms.NumberInput(attrs={'class': 'form-control-time'}),
            'time_of_move_in': forms.NumberInput(attrs={'class': 'form-control-time'}),
            'phone_number_1': forms.TextInput(attrs={'class': 'form-control-cont'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control-cont'}),
            'kakaotalk': forms.TextInput(attrs={'class': 'form-control-cont'}),
        }
