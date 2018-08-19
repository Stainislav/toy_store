from django.conf.urls import url, include
from products import views

urlpatterns = [
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
    url(r'^(?P<category_id>\w+)/$', views.products, name='products'),
]

