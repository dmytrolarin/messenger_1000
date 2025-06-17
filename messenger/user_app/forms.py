from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    '''
    Кастомізація форми для реєестрації, що базується на стандартній формі UserCreationForm
    '''
    username = forms.CharField(max_length=150, label="Логін",widget=forms.TextInput(attrs={"placeholder": "Логін","class": "form-field"}))
    password1 =forms.CharField(label="Пароль",widget=forms.PasswordInput(attrs={"placeholder": "Пароль", "class": "form-field"}))
    password2 =forms.CharField(label="Підтвердження пароля",widget=forms.PasswordInput(attrs={"placeholder": "Підтвердження пароля","class": "form-field"}))
    date_of_birth = forms.DateField(label="Дата народження", widget=forms.DateInput(attrs={"class":"form-field", "type":"date"}))
    avatar = forms.ImageField(label="Аватар профілю", required=False, widget=forms.FileInput(attrs={"class":"form-field"}))


class CustomAuthenticationForm(AuthenticationForm):
    '''
    Кастомізація форми для авторизації, що базується на стандартній формі AuthenticationForm
    '''
    username = forms.CharField(label="Логін", widget=forms.TextInput(attrs={"placeholder": "Логін", "class": "form-field" }))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"placeholder": "Пароль", "class": "form-field" }))