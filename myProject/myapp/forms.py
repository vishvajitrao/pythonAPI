from django.contrib.auth.models import User
from django import forms
from . models import Registration


class userForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter your username here'}))

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter your first name here'}))

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter your last name here'}))

    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter your email here'}))

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter your password here'}))

    confirmpass = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter your confirm password here'}))

    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


