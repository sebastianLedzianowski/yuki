from django import forms
from .models import Workshop

class WorkshopForm(forms.ModelForm):
    class Meta:
        model = Workshop
        fields = ['name', 'nip', 'regon', 'avatar']
