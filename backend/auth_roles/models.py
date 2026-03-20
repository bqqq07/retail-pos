from django.conf import settings
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Permission(models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.code


class UserRole(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_roles')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'role')

    def __str__(self) -> str:
        return f'{self.user_id}:{self.role_id}'


class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role_permissions')
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('role', 'permission')

    def __str__(self) -> str:
        return f'{self.role_id}:{self.permission_id}'
