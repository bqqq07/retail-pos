from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Employee


class EmployeeModelTests(TestCase):
    def test_employee_creation(self):
        user = get_user_model().objects.create_user(username='employee1', password='pass1234')
        employee = Employee.objects.create(
            user=user,
            full_name='Employee One',
            hire_date=date(2024, 1, 1),
        )
        self.assertEqual(employee.commission_type, 'none')
        self.assertTrue(employee.uuid)
