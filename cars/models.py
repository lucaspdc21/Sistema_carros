from django.db import models

class Car (models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=150)
    manufacturer = models.CharField(max_length=100)
    model_year = models.IntegerField(blank=True, null=True)
    factory_year = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)