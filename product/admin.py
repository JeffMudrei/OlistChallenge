from django.contrib import admin
from .models import Category, Product

class ProductInline(admin.TabularInline):
    model = Product
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ProductInline]

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'description', 'price']
#     list_editable = ['price']
