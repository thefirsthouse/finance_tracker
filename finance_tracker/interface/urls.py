from django.urls import path
import interface.views as views  # Можно оставить так или заменить на from . import views

urlpatterns = [
    path("", views.index, name='main'),
]
