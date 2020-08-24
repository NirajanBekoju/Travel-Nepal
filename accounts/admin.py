from django.contrib import admin
from .models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'is_agency')
    list_display_links = ('id', 'first_name', 'last_name', 'username', 'email')
    list_filter = ('is_agency',)
    search_fields = ('first_name', 'last_name', 'username')
    list_per_page = 25 

admin.site.register(Account, AccountAdmin)