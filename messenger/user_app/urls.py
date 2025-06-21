from .views import *
from django.urls import path

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', CustomLogoutView.as_view(), name = "logout"),
    path('update_avatar/', update_avatar, name = "update_avatar")
    # update_avatar
]