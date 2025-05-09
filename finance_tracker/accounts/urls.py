from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("login/", LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path("logout/", views.logout_user, name='logout'),
    path("register/", views.register, name='register'),
    path("profile/", views.profile, name='profile'),
    path("edit_profile/", views.edit_profile, name='edit_profile'),
]
