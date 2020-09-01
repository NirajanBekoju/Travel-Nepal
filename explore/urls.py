from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.explore, name="explore"),
    path('<int:id>', views.explore_event, name="explore_event"),
    path('<int:id>/inquire', views.event_inquiry, name="event_inquiry")
] 
