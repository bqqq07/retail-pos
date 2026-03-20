from django.contrib import admin

from .models import Permission, Role, RolePermission, UserRole


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ('name',)


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_select_related = ('user', 'role')


@admin.register(RolePermission)
class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ('role', 'permission')
    list_select_related = ('role', 'permission')
