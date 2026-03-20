from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.test import TestCase

from .models import Permission, Role, RolePermission, UserRole


class AuthRolesModelsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='tester', password='pass1234')

    def test_role_and_permission_can_be_created(self):
        role = Role.objects.create(name='Manager')
        permission = Permission.objects.create(code='sales.create_invoice', name='Create invoice')
        self.assertEqual(str(role), 'Manager')
        self.assertEqual(str(permission), 'sales.create_invoice')

    def test_user_role_is_unique(self):
        role = Role.objects.create(name='Cashier')
        UserRole.objects.create(user=self.user, role=role)
        with self.assertRaises(IntegrityError):
            UserRole.objects.create(user=self.user, role=role)

    def test_role_permission_is_unique(self):
        role = Role.objects.create(name='Owner')
        permission = Permission.objects.create(code='settings.view', name='View settings')
        RolePermission.objects.create(role=role, permission=permission)
        with self.assertRaises(IntegrityError):
            RolePermission.objects.create(role=role, permission=permission)
