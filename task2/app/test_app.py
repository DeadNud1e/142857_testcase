import unittest
from app import app
import json

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual("/product-category - all product - category pairs, /products all"+ \
                        " products with categories, /categories all categories with products" ,
                        response.get_data(as_text=True))

    def test_categories(self):
        response = self.client.get("/categories")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('categories', data.keys())
        self.assertNotEqual([], data['categories'])

    def test_products(self):
        response = self.client.get("/products")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('products', data.keys())
        self.assertNotEqual([], data['products'])

    def test_product_category(self):
        response = self.client.get("/product-category")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('product_category', data.keys())
        self.assertNotEqual([], data['product_category'])

if __name__ == "__main__":
    unittest.main()