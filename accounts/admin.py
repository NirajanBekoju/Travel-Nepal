from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'is_agency')
    list_display_links = ('id', 'first_name', 'last_name', 'username', 'email')
    list_filter = ('is_agency',)
    search_fields = ('first_name', 'last_name', 'username')
    list_per_page = 25 
    filter_horizontal = ()
    readonly_fields = ('date_joined','last_login')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal indo', {'fields':('first_name', 'last_name', 'username')}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'is_agency', 'is_staff', 'is_superuser')})
    )

admin.site.register(Account, AccountAdmin)