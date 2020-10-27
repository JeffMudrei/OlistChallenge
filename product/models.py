from django.db import models

class Category(models.Model):
   """
   Category Model
   Defines the attributes of a Category
   """
   name = models.CharField(max_length = 50)


class Product(models.Model):
    """
    Product Model
    Defines the attributes of a Product
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    price = models.DecimalField(max_digits=9,decimal_places=2)

    def get_category(self):
        """
        Function get_category
        Returns name and category of a product
        """
        return self.name + ' belongs to ' + str(self.category) + ' category.'
