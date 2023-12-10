from django import forms

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']  # 'user' 필드는 폼에서 제외
