from django.shortcuts import render
from products.models import Product, ProductImage, Category


def home(request):

    # Choose images for active products only.
    product_images = ProductImage.objects.filter(is_active=True, is_main=True)

    # Categories to show.
    boy_toys       = Category.objects.filter(parent__name="Игрушки для мальчиков")
    stuffed_toys   = Category.objects.filter(parent__name="Мягкие игрушки")
    girl_toys      = Category.objects.filter(parent__name="Игрушки для девочек")
    new_toys       = Category.objects.filter(name="Новинки")
    children_books = Category.objects.filter(name="Детские книги")
    hellium_balls  = Category.objects.filter(name="Гелиевые шары")

    # Images to show.
    stuffed_toys_images = product_images.filter(product__category__parent__name="Мягкие игрушки")
    boy_toys_images     = product_images.filter(product__category__parent__name="Игрушки для мальчиков")
    girl_toys_images    = product_images.filter(product__category__parent__name="Игрушки для девочек")

    return render(request, "home.html", locals())


def product(request, product_id):

    # Get product by ID.
    product = Product.objects.get(id=product_id)    

    # Choose images for active products only.
    product_images = ProductImage.objects.filter(is_active=True, is_main=True)

    # Images in the down of the product page.
    images_to_show = product_images.filter(product__category__name=product.category.name)
   
    return render(request, "product.html", locals())
