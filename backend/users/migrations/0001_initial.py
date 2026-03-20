import uuid

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('mobile', models.CharField(blank=True, max_length=20)),
                ('hire_date', models.DateField()),
                ('salary_basic', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('commission_type', models.CharField(choices=[('none', 'None'), ('sales', 'On Sales'), ('profit', 'On Profit'), ('collected', 'On Collected')], default='none', max_length=20)),
                ('commission_value', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
