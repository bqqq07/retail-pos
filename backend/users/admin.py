from django.contrib import admin

from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'mobile', 'hire_date', 'is_active')
    search_fields = ('full_name', 'mobile')
    list_filter = ('is_active', 'commission_type')
