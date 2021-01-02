from django.contrib import admin

from mdm_inventory.users.models import Client

# ADMIN to ProfileUser
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'dni',
        'phone_number',
        'address'
    )
    list_filter = ('phone_number',)