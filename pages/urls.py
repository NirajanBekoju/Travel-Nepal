from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard', views.user_dashboard, name="user_dashboard")
]
