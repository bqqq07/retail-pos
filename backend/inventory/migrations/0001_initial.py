import uuid

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_on_hand', models.DecimalField(decimal_places=3, default=0, max_digits=10)),
                ('avg_cost', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('last_purchase_cost', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryMovement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movement_type', models.CharField(choices=[('purchase', 'Purchase'), ('sale', 'Sale'), ('sale_return', 'Sale Return'), ('purchase_return', 'Purchase Return'), ('stocktake', 'Stocktake'), ('adjustment', 'Adjustment'), ('damage', 'Damage')], max_length=30)),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=10)),
                ('unit_cost', models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ('reference_type', models.CharField(blank=True, max_length=50)),
                ('reference_id', models.PositiveIntegerField(blank=True, null=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product')),
            ],
        ),
    ]
