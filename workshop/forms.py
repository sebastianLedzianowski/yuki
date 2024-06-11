from django import forms
from .models import Workshop

class WorkshopForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Workshop
        fields = ['name', 'nip', 'regon', 'address', 'phone', 'avatar']
