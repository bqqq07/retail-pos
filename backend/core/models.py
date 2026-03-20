import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


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
        return f"{self.code} - {self.name}"


class UserRole(models.Model):
    """مستخدم واحد يمكن أن يحمل أكثر من دور"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_roles')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'role')

    def __str__(self) -> str:
        return f'{self.user} -> {self.role}'


class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role_permissions')
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('role', 'permission')

    def __str__(self) -> str:
        return f'{self.role} -> {self.permission.code}'


class Employee(models.Model):
    COMMISSION_TYPES = [
        ('none', 'None'),
        ('sales', 'On Sales'),
        ('profit', 'On Profit'),
        ('collected', 'On Collected'),
    ]

    user = models.OneToOneField(User, on_delete=models.PROTECT)
    full_name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20, blank=True)
    hire_date = models.DateField()
    salary_basic = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    commission_type = models.CharField(max_length=20, choices=COMMISSION_TYPES, default='none')
    commission_value = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.full_name


class Device(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name} ({self.code})'


class AuditLog(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    action = models.CharField(max_length=50)
    model_name = models.CharField(max_length=100)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    object_repr = models.CharField(max_length=200, blank=True)
    changes = models.JSONField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f'{self.action} {self.model_name}'


class Settings(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()
    description = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.key
