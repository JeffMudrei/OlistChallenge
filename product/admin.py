from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Implements changes to the Category class
    Allows add new Category
    Allows delete new Categories
    """
    list_display = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Implements changes to the Product class
    Allows add new Products
    Allows  delete new products
    """
    list_display = ['name', 'description', 'price']
    list_editable = ['price']
