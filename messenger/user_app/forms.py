from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "ім'я","class": "form-field"}))
    password1 =forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "пароль", "class": "form-field"}))
    password2 =forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "підтвердження пароля","class": "form-field"}))
    
    class Meta:
        model = User
        fields = ["username","password1","password2"]