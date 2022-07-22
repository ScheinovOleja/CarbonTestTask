from django.contrib import admin

# Register your models here.
from delivery.models import DeliveryArea


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_coordinates']
    fields = ['name', 'coordinates']

    def get_coordinates(self, obj):
        areas = [zone for zone in obj.coordinates.keys()]
        return areas

    get_coordinates.short_description = 'Районы доставки'


admin.site.register(DeliveryArea, DeliveryAdmin)
