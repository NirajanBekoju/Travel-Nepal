from django.contrib import admin
from .models import Agency

class AgencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'agent_id', 'address', 'registered_date')
    list_display_links = ('name', )
    list_filter = ('is_active',)
    search_fields = ('name', 'agent_id', 'address')
    list_per_page = 25 

admin.site.register(Agency, AgencyAdmin)
