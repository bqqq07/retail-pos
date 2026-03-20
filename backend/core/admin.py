from django.contrib import admin

from .models import AuditLog, Device, SystemSetting


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active')
    search_fields = ('name', 'code')


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('action', 'model_name', 'object_id', 'user', 'created_at')
    search_fields = ('action', 'model_name', 'object_repr')
    list_filter = ('action', 'model_name')
    readonly_fields = (
        'user',
        'action',
        'model_name',
        'object_id',
        'object_repr',
        'changes',
        'ip_address',
        'created_at',
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(SystemSetting)
class SystemSettingAdmin(admin.ModelAdmin):
    list_display = ('key', 'updated_at')
    search_fields = ('key',)
