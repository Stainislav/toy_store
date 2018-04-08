from django.conf.urls import url
from product.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    #url(r'^organizations/$'
]

