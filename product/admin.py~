'''
from django.contrib import admin
from .models import (
    District,
    Category,
    EnterpriseNetwork,
    Organization,
    Goods,
    GoodsPriceConnection
    )


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_filter = ['id', 'name', 'description']
    search_fields = ['id', 'name', 'description']

    class Meta:
        model = Organization


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']
    search_fields = ['id', 'name']

    class Meta:
        model = District


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']
    search_fields = ['id', 'name']

    class Meta:
        model = Category


class EnterpriseNetworkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']
    search_fields = ['id', 'name']

    class Meta:
        model = EnterpriseNetwork


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    list_filter = ['id', 'name', 'category']
    search_fields = ['id', 'name', 'category']

    class Meta:
        model = Goods


class GoodsPriceConnectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'organization', 'goods', 'price']
    list_filter = ['id', 'organization', 'goods', 'price']
    search_fields = ['id', 'organization', 'goods', 'price']

    class Meta:
        model = GoodsPriceConnection


admin.site.register(District, DistrictAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(EnterpriseNetwork, EnterpriseNetworkAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodsPriceConnection, GoodsPriceConnectionAdmin)
'''
