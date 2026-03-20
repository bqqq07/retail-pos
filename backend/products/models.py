import uuid

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    full_name = models.CharField(max_length=300)
    sku = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL)
    parent_group = models.CharField(max_length=200, blank=True)
    scent = models.CharField(max_length=100, blank=True)
    size_label = models.CharField(max_length=50, blank=True)
    sale_price = models.DecimalField(max_digits=12, decimal_places=2)
    promo_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    min_stock = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    reorder_point = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    has_expiry = models.BooleanField(default=False)
    is_returnable = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.full_name


class ProductBarcode(models.Model):
    product = models.ForeignKey(Product, related_name='barcodes', on_delete=models.CASCADE)
    barcode = models.CharField(max_length=200, unique=True)
    is_primary = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.barcode
