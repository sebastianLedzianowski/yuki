from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django.core.validators import RegexValidator

from .models import ShopProfile


class RegisterForm(UserCreationForm):
    nip = forms.CharField(max_length=15,
                          validators=[
                              RegexValidator(
                                  regex=r'^\d+$',
                                  message='NIP should contain only digits.',
                              ),
                          ],
                          required=True,
                          help_text='Required. Please enter your Tax Identification Number.',
                          widget=forms.TextInput)

    email = forms.EmailField(max_length=254,
                             required=True,
                             help_text='Required. Please enter a valid email address.',
                             widget=forms.EmailInput())

    password1 = forms.CharField(max_length=50,
                                required=True,
                                help_text='Required. Please enter Password.',
                                widget=forms.PasswordInput())

    password2 = forms.CharField(max_length=50,
                                required=True,
                                help_text='Required. Please repeat your password.',
                                widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['nip', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['nip', 'password']


class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = ShopProfile
        fields = ['avatar']


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'}),
    )
