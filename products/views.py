from django.shortcuts import render
from products.models import Product, ProductImage


def index(request):
    products_images = ProductImage.objects.filter(is_active=True)
    return render(request, "base.html", locals())
