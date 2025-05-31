from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    '''
    Кастомізація форми для реєестрації, що базується на стандартній формі UserCreationForm
    '''
    username = forms.CharField(max_length=150, label="Логін",widget=forms.TextInput(attrs={"placeholder": "Логін","class": "form-field"}))
    password1 =forms.CharField(label="Пароль",widget=forms.PasswordInput(attrs={"placeholder": "Пароль", "class": "form-field"}))
    password2 =forms.CharField(label="Підтвердження пароля",widget=forms.PasswordInput(attrs={"placeholder": "Підтвердження пароля","class": "form-field"}))
    
    class Meta:
        model = User
        fields = ["username","password1","password2"]


class CustomAuthenticationForm(AuthenticationForm):
    '''
    Кастомізація форми для авторизації, що базується на стандартній формі AuthenticationForm
    '''
    username = forms.CharField(label="Логін", widget=forms.TextInput(attrs={"placeholder": "Логін", "class": "form-field" }))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"placeholder": "Пароль", "class": "form-field" }))