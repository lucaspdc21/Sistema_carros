from django.contrib import admin

from cars.models import Car

class CarAdmin (admin.ModelAdmin):
    list_display = ("model","manufacturer", "model_year", "value")
    search_fields = ("model", "model_year")


admin.site.register(Car,CarAdmin)