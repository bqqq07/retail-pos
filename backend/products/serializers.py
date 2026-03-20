from rest_framework import serializers

from .models import Brand, Category, Product, ProductBarcode


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'parent')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name')


class ProductBarcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBarcode
        fields = ('id', 'barcode', 'is_primary', 'is_active')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    barcodes = ProductBarcodeSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'full_name',
            'sku',
            'category',
            'brand',
            'parent_group',
            'scent',
            'size_label',
            'sale_price',
            'promo_price',
            'min_stock',
            'reorder_point',
            'has_expiry',
            'is_returnable',
            'is_active',
            'uuid',
            'created_at',
            'updated_at',
            'barcodes',
        )
