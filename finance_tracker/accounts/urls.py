from django.urls import path
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.views import LoginView, LogoutView

from .views import login, logout

urlpatterns = [
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout')
]