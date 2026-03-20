import uuid

from django.conf import settings
from django.db import models


class Employee(models.Model):
    COMMISSION_TYPES = [
        ('none', 'None'),
        ('sales', 'On Sales'),
        ('profit', 'On Profit'),
        ('collected', 'On Collected'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
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
