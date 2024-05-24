from django import forms
from .models import Repair

class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = ['car', 'workshop', 'description', 'start_date', 'end_date', 'cost', 'status', 'images', 'receipt', 'invoice']
