from rest_framework.test import APITestCase
from api.models import Product
import requests


class ShopApiTestCase(APITestCase):
    # def test_shop(self):
    #     client = self.client
    #     page_url = 'http://127.0.0.1:8000/api/v1/product/'
        
    #     result = client.get(page_url).status_code
        
    #     self.assertEqual(200, result)
    
    def test_shop2(self):
        page_url = 'http://127.0.0.1:8000/api/v1/product/58/'
        headers = {
            'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkzMzIzNTQwLCJpYXQiOjE2OTMzMjMyNDAsImp0aSI6Ijg3ZDc3NjJkMDlhZjRhZGI5NTFmZDUxYWQ4NjAyNThmIiwidXNlcl9pZCI6M30.2pMzLgK2IlqbstNsaP2lHMw8Kctb4_GB4dC1DKJJHhw'
        }
        
        result = requests.get(url=page_url, headers=headers).status_code
        
        self.assertEqual(200, result)