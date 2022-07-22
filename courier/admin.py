from django.contrib import admin


# Register your models here.
from courier.models import CourierDetail


class CourierAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'count_delivery']
    fields = ['name', 'surname', 'phone', 'area']

    def full_name(self, obj):
        return f"{obj.surname} {obj.name}"

    full_name.short_description = 'Имя курьера'


admin.site.register(CourierDetail, CourierAdmin)
