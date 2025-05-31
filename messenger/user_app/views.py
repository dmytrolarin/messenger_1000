from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomAuthenticationForm


class RegisterView(CreateView):
    '''
    Клас-відображення, який відповідає за відображення сторінки реєстрації
    '''
    # Вказуємо клас форми для відображення її на сторінці
    form_class = CustomUserCreationForm
    # Вказуємо шлях до шаблону сторінки
    template_name = "user_app/register.html"
    # Вказуємо url сторінки, на яку відбудеться перенаправлення після реєстрації
    success_url = reverse_lazy("login")

class CustomLoginView(LoginView):
    '''
    Клас, що відповідає за відображення стрінки логіну 
    '''
    template_name = "user_app/login.html"
    form_class = CustomAuthenticationForm

class CustomLogoutView(LogoutView):
    '''
    Цей клас-відображення відповідає за вихід з акаунту
    '''
    # Куди буде перенапрявляти після успішного виходу з акаунту
    next_page = "login" 