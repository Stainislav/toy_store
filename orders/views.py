from django.shortcuts import render
from django.http import JsonResponse
from orders.models import ProductInBasket 
from .forms import CheckoutContactForm
from django.contrib.auth.models import User
from .models import *
from products.models import Category


def basket_adding(request):

    return_dict = dict()
    
    session_key = request.session.session_key
    data        = request.POST
    product_id  = data.get("product_id")
    number      = data.get("number")
    is_delete   = data.get("is_delete")
    name        = data.get("name")
    
    if is_delete == 'true':
        TMP = ProductInBasket.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, is_active=True, product_id=product_id, defaults={'number':number})
        if not created:
            new_product.number += int(number)
            new_product.save(force_update=True)
    
    # Common code for two cases.
    products_in_basket                   = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_number                = products_in_basket.count()
    return_dict['products_total_number'] = products_total_number

    return_dict['products'] = list()

    for item in products_in_basket:
        product_dict                   = dict()
        product_dict['id']             = item.id
        product_dict['name']           = item.product.name
        product_dict['price_per_item'] = item.price_per_item
        product_dict['number']         = item.number
        return_dict['products'].append(product_dict)
 
    return JsonResponse(return_dict)


def checkout(request):

    session_key        = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    form               = CheckoutContactForm(request.POST or None)
    checkout_done      = False
    
    if request.POST:
        checkout_done = True
        if form.is_valid():
            data          = request.POST
            name          = data.get("name")
            phone         = data["phone"]
            user, created = User.objects.get_or_create(username=phone, defaults={'first_name': name})   
            order         = Order.objects.create(user=user, customer_name=name, customer_phone=phone)

            for name, value in data.items():
                if name.startswith("product_in_basket_"):
                    product_in_basket_id     = name.split("product_in_basket_")[1]
                    product_in_basket        = ProductInBasket.objects.get(id=product_in_basket_id)
                    product_in_basket.number = value
                    product_in_basket.order  = order
                    product_in_basket.save(force_update=True)

                    ProductInOrder.objects.create(product=product_in_basket.product, number=product_in_basket.number,
                                                                    price_per_item=product_in_basket.price_per_item,
                                                                    total_price=product_in_basket.total_price,
                                                                    order=order)
         
    return render(request, 'checkout.html', locals())


def cart(request):

    return render(request, 'cart.html', locals())

