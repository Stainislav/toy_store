'''
            Модель "Товары":
                -Название
                -Категория
                -Цена, может отличаться в зависимости от магазина
                -Описание
                -Отзывы
                -Магазин, в котором продаётся
                -Артикул
                -Производитель
                -Страна-производитель
'''

from django.db import models

# Категория.
class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

# Товар.
class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    manufacturer = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vendor_code = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

# Фотографии товаров.
class ProductImage(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
    name = models.CharField(max_length=100)
    #image = models.ImageField(upload_to='/products_images/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

