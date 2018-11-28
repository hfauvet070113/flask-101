from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2) # 2 is not a mistake here.
        self.assertEqual(response.status_code, 200)

    def test_get_products_json(self):
        response = self.client.get("/api/v1/products/1")
        products = response.json
        self.assertIsInstance(products, dict)
        self.assertEqual(response.status_code, 200)

    def test_add_product(self):
        response = self.client.post("/api/v1/products",
                                    json={"name": "toto"},
                                    content_type='application/json')
        product = response.json
        self.assertIsInstance(product, dict)
        self.assertEqual(product["name"], "toto")
        self.assertEqual(response.status_code, 201)

    def test_update_product(self):
        response = self.client.patch("/api/v1/products/1",
                                    json={"name": "titi"},
                                    content_type='application/json')
        product = response.json
        self.assertIsInstance(product, dict)
        self.assertEqual(product["id"], 1)
        self.assertEqual(product["name"], "titi")
        self.assertEqual(response.status_code, 204)
