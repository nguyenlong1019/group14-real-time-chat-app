from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Enter Username...",
        'class': '',
        'id': 'login-username',
        'required': True,
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Enter Password...",
        'class': '',
        'id': 'login-password',
        'required': True,
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Enter your username",
        'class': '',
        'id': '',
        'required': True,
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Enter your password",
        'class': '',
        'id': '',
        'required': True,
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Confirm Password",
        'class': '',
        'id': '',
        'required': True,
    }))