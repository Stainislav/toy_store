from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from products import views

urlpatterns = [
    url(r'^home/', views.home, name="home"),
    url(r'^admin/', admin.site.urls),
    url(r'^products/', include('products.urls')),
    #url(r'^', include('orders.urls')),
] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
