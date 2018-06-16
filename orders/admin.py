# Password 'pavel123'

from django.contrib import admin
from django.db import models
from orders.models import Status, Order, ProductInOrder


# Order status.
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']
    search_fields = ['id', 'name']

    class Meta:
        model = Status


# Order.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name']
    list_filter = ['id', 'customer_name']
    search_fields = ['id', 'customer_name']

    class Meta:
        model = Order


# Product in order.
class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_filter = ['id']
    search_fields = ['id']

    class Meta:
        model = ProductInOrder


admin.site.register(Status, StatusAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductInOrder, ProductInOrderAdmin)

