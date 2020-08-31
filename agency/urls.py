from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.agency_dashboard, name="agency_dashboard"),
    path('event/add', views.add_event, name="add_events"),
] 
