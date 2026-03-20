from django.conf import settings
from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class AuditLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
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


class SystemSetting(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()
    description = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.key
