from django.contrib import admin
from .models import Inquiry

# Register your models here.
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','last_name', 'email', 'phone', 'event_id', 'registered_date')
    list_display_links = ('id', 'first_name', 'last_name')
    list_filter = ('event_id',)
    search_fields = ('first_name', 'last_name', )
    list_per_page = 25 

admin.site.register(Inquiry, InquiryAdmin)