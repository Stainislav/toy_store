from django.test import Client
from django.test import TestCase

class RootPathViewTests(TestCase):
    def test_root(self):

        client = Client()
        response = self.client.get('/')
        
        self.assertEqual(response.status_code, 200)

    def test_products_path(self):

        client = Client()
        response = self.client.get('admin/')
        
        self.assertEqual(response.status_code, 200)

