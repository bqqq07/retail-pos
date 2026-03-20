from django.contrib import admin

from .models import InventoryBalance, InventoryMovement


@admin.register(InventoryBalance)
class InventoryBalanceAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity_on_hand', 'avg_cost', 'last_purchase_cost', 'updated_at')
    search_fields = ('product__full_name', 'product__sku')


@admin.register(InventoryMovement)
class InventoryMovementAdmin(admin.ModelAdmin):
    list_display = ('product', 'movement_type', 'quantity', 'unit_cost', 'created_by', 'created_at')
    search_fields = ('product__full_name', 'product__sku', 'reference_type')
    list_filter = ('movement_type',)
