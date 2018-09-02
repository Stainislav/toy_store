from django.conf.urls import url
from info import views

urlpatterns = [
    url(r'^about/', views.about, name='about'),
    url(r'^delivery/', views.delivery, name='delivery'),
    url(r'^adress/', views.adress, name='adress'),
    url(r'^refund/', views.refund, name='refund'),                         
]
