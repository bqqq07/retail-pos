from decimal import Decimal
from io import BytesIO

from django.test import TestCase
from openpyxl import Workbook
from rest_framework.test import APIClient

from .models import Brand, Category, Product
from .serializers import ProductSerializer


class ProductModelTests(TestCase):
    def test_product_with_promo_price(self):
        category = Category.objects.create(name='Body Care')
        brand = Brand.objects.create(name='Brand A')
        product = Product.objects.create(
            full_name='Lavender Lotion A 250ml',
            sku='SKU-001',
            category=category,
            brand=brand,
            sale_price=Decimal('50.00'),
            promo_price=Decimal('45.00'),
        )
        self.assertEqual(product.promo_price, Decimal('45.00'))


class ProductSerializerTests(TestCase):
    def test_product_serializer_fields(self):
        category = Category.objects.create(name='Hair Care')
        product = Product.objects.create(
            full_name='Shampoo X',
            sku='SKU-002',
            category=category,
            sale_price=Decimal('20.00'),
        )
        data = ProductSerializer(product).data
        self.assertEqual(data['sku'], 'SKU-002')
        self.assertIn('promo_price', data)


class ProductEndpointTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name='Skin Care')
        Product.objects.create(
            full_name='Aloe Gel',
            sku='SKU-003',
            category=self.category,
            sale_price=Decimal('30.00'),
        )

    def test_products_list_endpoint(self):
        response = self.client.get('/api/v1/products/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_products_search_endpoint(self):
        response = self.client.get('/api/v1/products/search/?q=Aloe')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_products_import_endpoint(self):
        workbook = Workbook()
        sheet = workbook.active
        sheet.append(['full_name', 'sku', 'category', 'brand', 'sale_price'])
        sheet.append(['Rose Mist', 'SKU-004', 'Skin Care', 'Brand B', '35.00'])

        payload = BytesIO()
        workbook.save(payload)
        payload.seek(0)
        payload.name = 'products.xlsx'

        response = self.client.post(
            '/api/v1/products/import/',
            {'file': payload},
            format='multipart',
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['created'], 1)
