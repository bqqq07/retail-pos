from rest_framework import serializers

from .models import InventoryBalance, InventoryMovement


class InventoryBalanceSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.full_name', read_only=True)
    sku = serializers.CharField(source='product.sku', read_only=True)

    class Meta:
        model = InventoryBalance
        fields = (
            'id',
            'product',
            'product_name',
            'sku',
            'quantity_on_hand',
            'avg_cost',
            'last_purchase_cost',
            'updated_at',
        )


class InventoryMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryMovement
        fields = (
            'id',
            'product',
            'movement_type',
            'quantity',
            'unit_cost',
            'reference_type',
            'reference_id',
            'notes',
            'created_by',
            'created_at',
            'uuid',
        )
