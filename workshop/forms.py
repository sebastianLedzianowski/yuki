from django import forms
from .models import Workshop

class WorkshopForm(forms.ModelForm):

    class Meta:
        model = Workshop
        fields = ['email', 'phone', 'avatar']


class CEIDGSearchForm(forms.Form):
    nip = forms.CharField(label='NIP', max_length=10, required=True, help_text='Enter NIP number')