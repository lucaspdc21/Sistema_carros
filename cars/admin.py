from django.contrib import admin

from cars.models import Car, Manufacturer

class CarAdmin (admin.ModelAdmin):
    list_display = ("model","manufacturer", "model_year", "value")
    search_fields = ("model", "model_year")

class ManufacturerAdmin (admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

admin.site.register(Car,CarAdmin)
admin.site.register(Manufacturer ,ManufacturerAdmin)