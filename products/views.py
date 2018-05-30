from django.shortcuts import render
from products.models import Product, ProductImage, Category


def home(request):
    products_images = ProductImage.objects.filter(is_active=True)

    parent_names = Category.objects.filter(parent__name=None)
    stuffed_toys = Category.objects.filter(parent__name="Мягкие игрушки")

    # Categories to show.
    boy_toys = Category.objects.filter(parent__name="Игрушки для мальчиков")
    girl_toys = Category.objects.filter(parent__name="Игрушки для девочек")
    new_toys = Category.objects.filter(name="Новинки")
    special_for_you_toys = Category.objects.filter(name="Специально для вас")

    # Images to show.
    stuffed_toys_images = ProductImage.objects.filter(product__category__parent__name="Мягкие игрушки")
    boy_toys_images = ProductImage.objects.filter(product__category__parent__name="Игрушки для мальчиков")
    toys_for_girl_images = products_images.filter(product__category__parent__name="Игрушки для девочек")
    girl_toys_images = toys_for_girl_images.filter(product__new=False)

    girl_new_toys_images = toys_for_girl_images.filter(product__new=True)
    special_for_you_toys_images = products_images.filter(product__category__name="Специально для вас")

    return render(request, "home.html", locals())

