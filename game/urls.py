# game/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start_game, name='start_game'),
    path('guess/', views.make_guess, name='make_guess'),
    path('api/sample/', views.sample_api, name='sample_api'),
]
