from django import forms
from .models import UserPreferences


class PositiveCheckListForm(forms.ModelForm):
    class Meta:
        exclude = ['user']
        model = UserPreferences
        widgets = {
            'sports': forms.CheckboxSelectMultiple(attrs={'class': 'sports'}),
            'music': forms.CheckboxSelectMultiple(attrs={'class': 'music'}),
            'arts_crafts': forms.CheckboxSelectMultiple(attrs={'class': 'arts-crafts'}),
            'reading': forms.CheckboxSelectMultiple(attrs={'class': 'reading'}),
            'cooking': forms.CheckboxSelectMultiple(attrs={'class': 'cooking'}),
            'movies_tv': forms.CheckboxSelectMultiple(attrs={'class': 'movies-tv'}),
            'gaming': forms.CheckboxSelectMultiple(attrs={'class': 'gaming'}),
            'traveling': forms.CheckboxSelectMultiple(attrs={'class': 'traveling'}),
            'language_learning': forms.CheckboxSelectMultiple(attrs={'class': 'language-learning'}),
            'outdoor_activities': forms.CheckboxSelectMultiple(attrs={'class': 'outdoor-activities'}),
            'fitness': forms.CheckboxSelectMultiple(attrs={'class': 'fitness'}),
            'technology': forms.CheckboxSelectMultiple(attrs={'class': 'technology'}),
            'social_activities': forms.CheckboxSelectMultiple(attrs={'class': 'social-activities'}),
            'meditation': forms.CheckboxSelectMultiple(attrs={'class': 'meditation'}),
            'pet_care': forms.CheckboxSelectMultiple(attrs={'class': 'pet-care'}),
            # Add other fields as needed
        }
