from django import forms
from .models import WorkshopProfile

class WorkshopProfileForm(forms.ModelForm):
    class Meta:
        model = WorkshopProfile
        fields = ['name', 'nip', 'regon', 'avatar']
