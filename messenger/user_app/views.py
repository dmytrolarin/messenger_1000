from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.views import LoginView,LogoutView
from django.http import JsonResponse
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import Profile


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

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        date_of_birth = form.cleaned_data.get("date_of_birth")
        avatar = form.cleaned_data.get("avatar")
        Profile.objects.create(user = user, date_of_birth = date_of_birth, avatar = avatar)
        return response

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


def update_avatar(request):
    avatar = request.FILES.get('avatar')
    profile = Profile.objects.get(user=request.user)
    profile.avatar = avatar
    profile.save()
    return JsonResponse({'success':True, 'avatar_url': profile.avatar.url})