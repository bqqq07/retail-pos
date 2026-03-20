import uuid

from django.conf import settings
from django.db import models

from products.models import Product

MOVEMENT_TYPES = [
    ('purchase', 'Purchase'),
    ('sale', 'Sale'),
    ('sale_return', 'Sale Return'),
    ('purchase_return', 'Purchase Return'),
    ('stocktake', 'Stocktake'),
    ('adjustment', 'Adjustment'),
    ('damage', 'Damage'),
]


class InventoryBalance(models.Model):
    product = models.OneToOneField(Product, on_delete=models.PROTECT)
    quantity_on_hand = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    avg_cost = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    last_purchase_cost = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.product_id}'


class InventoryMovement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    movement_type = models.CharField(max_length=30, choices=MOVEMENT_TYPES)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    unit_cost = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    reference_type = models.CharField(max_length=50, blank=True)
    reference_id = models.PositiveIntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    def __str__(self) -> str:
        return f'{self.product_id}:{self.movement_type}'
