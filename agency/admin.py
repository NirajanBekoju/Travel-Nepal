from django.contrib import admin
from .models import Agency, Event

class AgencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'agent_id', 'address', 'registered_date')
    list_display_links = ('name', )
    list_filter = ('is_active',)
    search_fields = ('name', 'agent_id', 'address')
    list_per_page = 25 


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'agency_id', 'location', 'is_display', 'registered_date', 'booking_date_limit')
    list_display_links = ('title', )
    list_filter = ('is_display', 'agency_id')
    search_fields = ('title', 'agency_id', 'location')
    list_per_page = 25 

admin.site.register(Agency, AgencyAdmin)
admin.site.register(Event, EventAdmin)
