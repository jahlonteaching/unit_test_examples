import unittest

from examples.ecommerce import Product, Customer, Payment


class TestEcommerce(unittest.TestCase):
    def setUp(self):
        self.product = Product("Test Product", 10, 100)
        self.customer = Customer("Test Customer", "test@example.com")

    def test_purchase_product(self):
        self.product.purchase(1)
        self.assertEqual(self.product.stock, 99)

    def test_purchase_insufficient_stock(self):
        with self.assertRaises(ValueError):
            self.product.purchase(101)

    def test_add_to_cart(self):
        self.customer.add_to_cart(self.product, 2)
        self.assertEqual(len(self.customer.cart), 1)

    def test_remove_from_cart(self):
        self.customer.add_to_cart(self.product, 2)
        self.customer.remove_from_cart(self.product)
        self.assertEqual(len(self.customer.cart), 0)

    def test_remove_nonexistent_product_from_cart(self):
        with self.assertRaises(ValueError):
            self.customer.remove_from_cart(self.product)

    def test_checkout(self):
        self.customer.add_to_cart(self.product, 2)
        order = self.customer.checkout()
        self.assertEqual(len(self.customer.cart), 0)
        self.assertEqual(len(order.products), 1)
        self.assertEqual(order.total, 20)

    def test_checkout_insufficient_stock(self):
        self.product.stock = 0
        self.customer.add_to_cart(self.product, 2)
        with self.assertRaises(ValueError):
            self.customer.checkout()

    def test_process_payment(self):
        self.customer.add_to_cart(self.product, 2)
        order = self.customer.checkout()
        payment = Payment(order, 20)
        payment.process()

    def test_process_incorrect_payment(self):
        self.customer.add_to_cart(self.product, 2)
        order = self.customer.checkout()
        payment = Payment(order, 19)
        with self.assertRaises(ValueError):
            payment.process()


if __name__ == '__main__':
    unittest.main()
