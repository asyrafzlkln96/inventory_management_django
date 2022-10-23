from django.test import TestCase, Client
import unittest
from .models import Inventory
# Create your tests here.
class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_inventory(self):
        # Issue a GET request.
        response = self.client.get('/inventory')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        print('Endpoint /inventory is OK')

    def test_all_by_inventories(self):
    	# Issue a GET request.
        response = self.client.get('/api/inventory')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        print('Endpoint /api/inventory is OK')

    def test_get_inventory_by_id(self):
    	# Issue a GET request.
    	inventory_id = 3
    	response = self.client.get('/inventory/{}'.format(inventory_id), follow=True)
    	# Check that the response is 200 OK.
    	self.assertEqual(response.status_code, 200)
    	print('Endpoint /inventory/<id> is OK')