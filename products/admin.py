# Password 'pavel123'

from django.contrib import admin
from django.db import models
from products.models import Category


# Категория.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']
    search_fields = ['id', 'name']

    class Meta:
        model = Category

'''
# Товар.
class ProductAdmin(models.Model):
    list_display = ['id', 'name', 'description']
    list_filter = ['id', 'name', 'description']
    search_fields = ['id', 'name', 'description']

    class Meta:
        model = Product


# Фотографии товаров.
class ProductImageAdmin(models.Model):
    list_display = ['id', 'name', 'description']
    list_filter = ['id', 'name', 'description']
    search_fields = ['id', 'name', 'description']

    class Meta:
        model = ProductImageAdmin
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)

'''
admin.site.register(Category, CategoryAdmin)

