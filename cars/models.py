from django.db import models

class Manufacturer (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Car (models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=150)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, related_name="car_manufacturer")
    model_year = models.IntegerField(blank=True, null=True)
    factory_year = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.model