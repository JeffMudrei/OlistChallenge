from django.test import TestCase
from ..models import Product, Category

class ProductTest(TestCase):
    """
    Test module for Product model
    """

    def setUp(self):
        """
        Adding test entries to the product table.
        """
        electronics = Category.objects.create(name='Electronics')
        tv = Product.objects.create(name='tv', description='tv lcd', price=299.99)
        radio = Product.objects.create(name='radio', description='radio gaga', price=399.99)

        tv.category.add(electronics)
        radio.category.add(electronics)

    def test_product_category(self):
        """
        Confirming that the 'get_category ()' method returned the correct string.
        """
        product_tv = Product.objects.get(name='tv')
        product_radio = Product.objects.get(name='radio')
        self.assertEqual(product_tv.get_category(), "tv belongs to Electronics category.")
        self.assertEqual(product_radio.get_category(), "radio belongs to Electronics category.")
