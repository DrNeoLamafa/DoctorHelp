from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=150,
        label='Имя пользователя',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': ''
        })
    )
    password1 = forms.CharField(
        max_length=128,
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': ''
        })
    )
    password2 = forms.CharField(
        max_length=128,
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': ''
        })
    )
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')


class LoginForm(AuthenticationForm):

    
    username = forms.EmailField(
        max_length=150,
        label='Имя пользователя',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': ''
        })
    )
    password = forms.CharField(
        max_length=128,
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': ''
        })
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
    



