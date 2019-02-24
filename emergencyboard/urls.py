from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='emergencyboard/home'),
    path('random-link', views.random_link, name='emergencyboard/random_link'),
]
