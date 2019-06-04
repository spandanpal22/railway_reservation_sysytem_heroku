from django.contrib.auth.models import User
from django import forms
from .models import UserRegistration

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User

        fields=['username','email','password']


"""
class SignUpForm(forms.ModelForm):
    class Meta:
        model=UserRegistration

        fields=['firstName','lastName','address','gender','dob','mobileNumber','occupation']
"""