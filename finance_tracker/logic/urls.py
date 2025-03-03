from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("create_account/", views.create_account, name='create_account'),
    path("create_transfer/", views.create_transfer, name='create_transfer'),
]
