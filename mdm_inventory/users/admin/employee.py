from django.contrib import admin
from mdm_inventory.users.models import Employee

# ADMIN to ProfileUser
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'date_of_birth',
        'entry_date',
        'salary',
        'is_manager',
        'is_cashier',
        'is_supervisor'
    )
    list_filter = ('is_manager','is_cashier','is_supervisor',)