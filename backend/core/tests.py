from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import AuditLog, Device, SystemSetting


class CoreModelTests(TestCase):
    def test_device_creation(self):
        device = Device.objects.create(name='Main POS', code='POS-01')
        self.assertEqual(str(device), 'Main POS')

    def test_system_setting_creation(self):
        setting = SystemSetting.objects.create(key='vat_rate', value='15.00')
        self.assertEqual(setting.key, 'vat_rate')

    def test_audit_log_ordering(self):
        user = get_user_model().objects.create_user(username='auditor', password='pass1234')
        log = AuditLog.objects.create(user=user, action='login', model_name='User')
        self.assertEqual(str(log), 'login User')
