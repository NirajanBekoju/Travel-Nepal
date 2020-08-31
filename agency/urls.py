from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.agency_dashboard, name="agency_dashboard"),
    path('event/add', views.add_event, name="add_events"),
    path('event/<int:id>/show', views.show_event, name="show_event"),
    path('event/<int:id>/update', views.update_event, name="update_event"),
    path('event/<int:id>/delete', views.delete_event, name="delete_event"),
] 
