from django import forms
from .models import ShopProfile

class ShopProfileForm(forms.ModelForm):
    class Meta:
        model = ShopProfile
        fields = ['shop_name', 'nip', 'regon', 'avatar']
