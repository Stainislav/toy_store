from django.contrib import admin
from info.models import InfoPage


# Information page.
class InfoPageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'text']
    list_filter = ['id', 'name', 'text']
    search_fields = ['id', 'name', 'text']

    class Meta:
        model = InfoPage


admin.site.register(InfoPage, InfoPageAdmin)

