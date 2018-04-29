from django.db import models
from products.models import Product

# Статус заказа.
class Status(models.Model):

    name = models.CharField(max_length=30, blank=True, null=True, default=None)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    comments = models.TextField(max_length=500, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы заказов"


# Заказ.
class Order(models.Model):

    customer_name = models.CharField(max_length=200, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=50, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    comments = models.TextField(max_length=500, blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.status) 

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


# Товар в заказе.
class ProductInOrder(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)     
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

