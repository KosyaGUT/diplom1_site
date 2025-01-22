from django import forms
from django.contrib.auth.forms import AuthenticationForm

from authentication.models import User


class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'input-box',
        'type': 'email',
        'id': 'email',  # Добавляем id
        'placeholder': 'Введите почту',
        'required': 'required'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-box',
        'type': 'password',
        'id': 'password',
        'placeholder': 'Введите пароль',
        'required': 'required'
    }))
    remember_me = forms.BooleanField(
        required=False,  # Чекбокс необязателен
        widget=forms.CheckboxInput(attrs={
            'class': 'custom-checkbox',
            'id': 'rememberMereg',
        })
    )

    class Meta:
        model = User
        fields = ('email', 'password')
