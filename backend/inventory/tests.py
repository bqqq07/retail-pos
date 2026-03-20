from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from products.models import Category, Product

from .models import InventoryBalance, InventoryMovement
from .serializers import InventoryBalanceSerializer


class InventoryModelTests(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Body Care')
        self.product = Product.objects.create(
            full_name='Mint Cream',
            sku='SKU-INV-001',
            category=category,
            sale_price=Decimal('10.00'),
        )

    def test_inventory_balance_creation(self):
        balance = InventoryBalance.objects.create(product=self.product, quantity_on_hand=Decimal('5.000'))
        self.assertEqual(balance.quantity_on_hand, Decimal('5.000'))

    def test_inventory_movement_creation(self):
        user = get_user_model().objects.create_user(username='inv-user', password='pass1234')
        movement = InventoryMovement.objects.create(
            product=self.product,
            movement_type='purchase',
            quantity=Decimal('2.000'),
            created_by=user,
        )
        self.assertEqual(movement.movement_type, 'purchase')
        self.assertTrue(movement.uuid)


class InventorySerializerTests(TestCase):
    def test_inventory_balance_serializer(self):
        category = Category.objects.create(name='Hair Care')
        product = Product.objects.create(
            full_name='Hair Oil',
            sku='SKU-INV-002',
            category=category,
            sale_price=Decimal('15.00'),
        )
        balance = InventoryBalance.objects.create(product=product, quantity_on_hand=Decimal('1.000'))
        data = InventoryBalanceSerializer(balance).data
        self.assertEqual(data['sku'], 'SKU-INV-002')


class InventoryEndpointTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        category = Category.objects.create(name='Low Stock Cat')
        product = Product.objects.create(
            full_name='Low Stock Product',
            sku='SKU-INV-003',
            category=category,
            sale_price=Decimal('5.00'),
        )
        InventoryBalance.objects.create(product=product, quantity_on_hand=Decimal('0.000'))

    def test_low_stock_endpoint(self):
        response = self.client.get('/api/v1/inventory/low-stock/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_forecast_critical_placeholder_endpoint(self):
        response = self.client.get('/api/v1/inventory/forecast/critical/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])
