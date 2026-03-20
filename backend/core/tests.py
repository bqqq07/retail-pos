from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import (
    AuditLog,
    Device,
    Employee,
    Permission,
    Role,
    RolePermission,
    Settings,
    UserRole,
)


class CoreModelsTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester',
            email='tester@example.com',
            password='password123',
        )

    def test_role_creation(self):
        role = Role.objects.create(name='Manager')
        self.assertEqual(role.name, 'Manager')

    def test_permission_creation(self):
        permission = Permission.objects.create(code='sales.create_invoice', name='Create Invoice')
        self.assertEqual(permission.code, 'sales.create_invoice')

    def test_user_role_unique_constraint(self):
        role = Role.objects.create(name='Cashier')
        UserRole.objects.create(user=self.user, role=role)
        with self.assertRaises(Exception):
            UserRole.objects.create(user=self.user, role=role)

    def test_role_permission_unique_constraint(self):
        role = Role.objects.create(name='Owner')
        permission = Permission.objects.create(code='users.manage', name='Manage Users')
        RolePermission.objects.create(role=role, permission=permission)
        with self.assertRaises(Exception):
            RolePermission.objects.create(role=role, permission=permission)

    def test_employee_uuid_is_generated(self):
        employee = Employee.objects.create(
            user=self.user,
            full_name='Test Employee',
            hire_date=date(2025, 1, 1),
        )
        self.assertIsNotNone(employee.uuid)

    def test_device_creation(self):
        device = Device.objects.create(name='POS-1', code='POS-001')
        self.assertEqual(device.code, 'POS-001')

    def test_audit_log_ordering(self):
        AuditLog.objects.create(action='login', model_name='User', user=self.user)
        AuditLog.objects.create(action='logout', model_name='User', user=self.user)
        logs = AuditLog.objects.all()
        self.assertEqual(logs[0].action, 'logout')

    def test_settings_creation(self):
        setting = Settings.objects.create(key='business_name', value='Retail POS')
        self.assertEqual(setting.key, 'business_name')
