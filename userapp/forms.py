from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    avatar = forms.ImageField(label='Аватар')
    phone_number = forms.CharField(label='Номер телефона')
    country = forms.CharField(label='Страна')


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

class EmailVerificationForm(forms.Form):
    verification_code = forms.CharField(label='Код верификации')

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='Email')
