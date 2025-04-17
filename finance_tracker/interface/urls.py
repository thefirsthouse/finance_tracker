from django.urls import path
import interface.views as views  # Можно оставить так или заменить на from . import views
import logic.views as logic_views

urlpatterns = [
    path("", views.index, name='main'),
    path("records/", views.records_list, name='records'),
    path("records/create", logic_views.create_transfer, name='create_transfer'),
]
