from django.db import models

class Category(models.Model):
   """
   Category Model
   Defines the attributes of a Category
   """
   name = models.CharField(max_length = 50)

   def __str__(self):
       return self.name


class Product(models.Model):
    """
    Product Model
    Defines the attributes of a Product
    """
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    price = models.DecimalField(max_digits=9,decimal_places=2)

    def __str__(self):
        return self.name

    def get_category(self):
        """
        Function get_category
        Returns name and category of a product
        """
        return self.name + ' belongs to ' + self.category.first().name + ' category.'
