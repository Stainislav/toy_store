from django.shortcuts import render
from products.models import Product, ProductImage, Category


def home(request):

    # Categories to show.
    boy_toys       = Category.objects.filter(parent__name="Игрушки для мальчиков")
    stuffed_toys   = Category.objects.filter(parent__name="Мягкие игрушки")
    girl_toys      = Category.objects.filter(parent__name="Игрушки для девочек")
    new_toys       = Category.objects.filter(name="Новинки")
    children_books = Category.objects.filter(name="Детские книги")
    hellium_balls  = Category.objects.filter(name="Гелиевые шары")

    # Images to show.
    stuffed_toys_images = ProductImage.objects.filter(product__category__parent__name="Мягкие игрушки")
    boy_toys_images     = ProductImage.objects.filter(product__category__parent__name="Игрушки для мальчиков")
    girl_toys_images    = ProductImage.objects.filter(product__category__parent__name="Игрушки для девочек")

    return render(request, "home.html", locals())

