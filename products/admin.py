# Password 'pavel123'

from django.contrib import admin
from django.db import models
from products.models import Category, Product, ProductImage


# Inline class for image of a product.
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


# Category.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']
    search_fields = ['id', 'name']

    class Meta:
        model = Category


# Product.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_filter = ['id', 'name', 'description', 'category']
    search_fields = ['id', 'name', 'description']

    inlines = [ProductImageInline]    

    class Meta:
        model = Product


# Product photos.
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']
    search_fields = ['id', 'name']

    class Meta:
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
