from django.test import TestCase
from django.contrib.auth.models import User


class ModelPrefixTestCase(TestCase):
    def test_model_prefix(self):
        """Check if the table prefix that is set in the settings is being used"""
        table_name = User.objects.model._meta.db_table
        self.assertEqual(table_name, 'foo_auth_user')
