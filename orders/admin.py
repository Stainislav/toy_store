# Password 'pavel123'

from django.contrib import admin
from django.db import models
from orders.models import Status, Order, ProductInOrder, ProductInBasket



# Inline class for image of a product.
class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


# Order status.
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']
    search_fields = ['id', 'name']

    class Meta:
        model = Status


# Order.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'customer_phone', 'customer_email', 'user']
    list_filter = ['id', 'customer_name']
    search_fields = ['id', 'customer_name']

    inlines = [ProductInOrderInline]

    class Meta:
        model = Order


# Product in order.
class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order']
    list_filter = ['id']
    search_fields = ['id']

    class Meta:
        model = ProductInOrder


# Product in basket.
class ProductInBasketAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'price_per_item', 'total_price', 'product', 'is_active']
    list_filter = ['id']
    search_fields = ['id']

    class Meta:
        model = ProductInBasket

admin.site.register(Status, StatusAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductInOrder, ProductInOrderAdmin)
admin.site.register(ProductInBasket, ProductInBasketAdmin)

