from django.db import models

# Category.
class Category(models.Model):

    name   = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='child')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = "Категория"
        verbose_name_plural = "Категории"

# Product.
class Product(models.Model):

    name            = models.CharField(max_length=100)
    description     = models.TextField(max_length=1100)
    manufacturer    = models.CharField(max_length=50)
    price           = models.DecimalField(max_digits=10, decimal_places=2)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    vendor_code     = models.CharField(max_length=50)
    country         = models.CharField(max_length=50)
    is_active       = models.BooleanField(default=True)
    new             = models.BooleanField(default=True)
    special_for_you = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = "Товар"
        verbose_name_plural = "Товары"

# Product images.
class ProductImage(models.Model):
    
    product   = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
    name      = models.CharField(max_length=100)
    image     = models.ImageField(upload_to='products_images/', blank=True)
    is_main   = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name        = "Фотография"
        verbose_name_plural = "Фотографии"

