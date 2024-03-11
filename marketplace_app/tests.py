# marketplace_app/tests.py

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Product

class MarketplaceAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword',
            phone_number='1234567890'
        )


    def test_product_creation(self):
        self.client.force_authenticate(user=self.user)

        url = '/api/products/'
        data = {
            'name': 'Test Product',
            'description': 'This is a test product.',
            'price': '19.99',
            'seller': 1
        }

        # Open the image file in binary mode
        with open('G:/marketplace/market_place/product_images/Share.png', 'rb') as image_file:

            # Attach the image to the data
            data['image'] = image_file

            response = self.client.post(url, data, format='multipart')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Product.objects.count(), 1)
            self.assertEqual(Product.objects.first().name, 'Test Product')


    def test_purchase_creation(self):
        # Assuming you have sellers and buyers for testing
        seller = get_user_model().objects.create_user(username='seller', email='seller@example.com', password='sellerpassword')
        buyer = get_user_model().objects.create_user(username='buyer', email='buyer@example.com', password='buypassword')

        # Authenticate the buyer
        self.client.force_authenticate(user=buyer)

        # Create a product for testing
        product = Product.objects.create(name='Test Product', description='This is a test product.', price=19.99, seller=seller)

        url = f'/api/purchase/'
        data = {
            'product': product.id,
            'seller': seller.id,
            'buyer': buyer.id,
            'purchase_price': '19.99',
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)