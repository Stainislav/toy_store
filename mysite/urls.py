from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('products.urls')),
    #url(r'^', include('orders.urls')),
    url(r'^admin/', admin.site.urls),
]

