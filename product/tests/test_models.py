from django.test import TestCase
from ..models import Product

class ProductTest(TestCase):
    """
    Test module for Product model
    """

    def setUp(self):
        """
        Adding test entries to the product table.
        """
        Product.objects.create(name='tv', description='tv lcd', price=299.99, category=1)
        Product.objects.create(name='radio', description='radio gaga', price=399.99, category=2)

    def test_product_category(self):
        """
        Confirming that the 'get_category ()' method returned the correct string.
        """
        product_tv = Product.objects.get(name='tv')
        product_radio = Product.objects.get(name='radio') 
        self.assertEqual(product_tv.get_category(), "tv belongs to 1 category.")
        self.assertEqual(product_radio.get_category(), "radio belongs to 2 category.")



