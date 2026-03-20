from django.contrib import admin

from .models import Brand, Category, Product, ProductBarcode


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ProductBarcodeInline(admin.TabularInline):
    model = ProductBarcode
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'sku', 'category', 'brand', 'sale_price', 'promo_price', 'is_active')
    search_fields = ('full_name', 'sku')
    list_filter = ('is_active', 'category', 'brand')
    inlines = [ProductBarcodeInline]


@admin.register(ProductBarcode)
class ProductBarcodeAdmin(admin.ModelAdmin):
    list_display = ('barcode', 'product', 'is_primary', 'is_active')
    search_fields = ('barcode', 'product__full_name', 'product__sku')
    list_filter = ('is_primary', 'is_active')
