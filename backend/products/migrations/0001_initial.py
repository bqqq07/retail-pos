import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=300)),
                ('sku', models.CharField(max_length=100, unique=True)),
                ('parent_group', models.CharField(blank=True, max_length=200)),
                ('scent', models.CharField(blank=True, max_length=100)),
                ('size_label', models.CharField(blank=True, max_length=50)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('promo_price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('min_stock', models.DecimalField(decimal_places=3, default=0, max_digits=10)),
                ('reorder_point', models.DecimalField(decimal_places=3, default=0, max_digits=10)),
                ('has_expiry', models.BooleanField(default=False)),
                ('is_returnable', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductBarcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=200, unique=True)),
                ('is_primary', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barcodes', to='products.product')),
            ],
        ),
    ]
