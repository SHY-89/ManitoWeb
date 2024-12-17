from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',  
                'placeholder': '아이디를 입력하세요', 
            }
        ),
        label=''  
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',  
                'placeholder': '비밀번호를 입력하세요',  
            }
        ),
        label=''  
    )


class CustomUserCreationForm(UserCreationForm):  
    class Meta:
        model = get_user_model()
        fields = [
            "username", 
            "first_name",
            "last_name",
            "email",
        ]

        labels = {
            "username": "아이디",
            "first_name": "성함",
            "last_name": "닉네임",
            "email": "email",
        }

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label=_("아이디"),
        widget=forms.TextInput(attrs={"autofocus": True}),
    )


class CustomUserChangeForm(UserChangeForm):
    password = None
    
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email")
        labels = {
            "first_name": "성함",
            "last_name": "닉네임",
            "email": "email",
        }

