from django.db import models
from products.models import Product
from django.contrib.auth.models import User


# Order status.
class Status(models.Model):

    name      = models.CharField(max_length=30, blank=True, null=True, default=None)
    updated   = models.DateTimeField(auto_now_add=False, auto_now=True)
    comments  = models.TextField(max_length=500, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name        = "Статус"
        verbose_name_plural = "Статусы заказов"


# Order.
class Order(models.Model):

    user           = models.ForeignKey(User, blank=True, null=True, default=False, on_delete=models.CASCADE)
    customer_name  = models.CharField(max_length=200, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=50, blank=True, null=True, default=None)
    created        = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated        = models.DateTimeField(auto_now_add=False, auto_now=True)
    comments       = models.TextField(max_length=500, blank=True, null=True, default=None)
    status         = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.status) 

    class Meta:
        verbose_name        = "Заказ"
        verbose_name_plural = "Заказы"


# Product in order.
class ProductInOrder(models.Model):

    order          = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, default=None)
    number         = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price    = models.DecimalField(max_digits=10, decimal_places=2, default=0)#price*nmb
    product        = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)     
    created        = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated        = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active      = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name        = "Товар"
        verbose_name_plural = "Товары"

    def save(self, *args, **kwargs):
        price_per_item      = self.product.price
        self.price_per_item = price_per_item
        self.total_price    = int(self.number) * price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)


# Product in basket.
class ProductInBasket(models.Model):

    session_key    = models.CharField(max_length=128, blank=True, null=True, default=None)
    number         = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price    = models.DecimalField(max_digits=10, decimal_places=2, default=0)    
    order          = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, default=None)
    product        = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)    
    created        = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated        = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active      = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name        = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"

    def save(self, *args, **kwargs):
        price_per_item      = self.product.price
        self.price_per_item = price_per_item
        self.total_price    = int(self.number) * price_per_item

        super(ProductInBasket, self).save(*args, **kwargs)

