from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("register/", views.register, name='register'),
    path("profile/", views.profile, name='profile'),
    path("edit_profile/", views.edit_profile, name='edit_profile'),  # Добавьте этот путь
]
