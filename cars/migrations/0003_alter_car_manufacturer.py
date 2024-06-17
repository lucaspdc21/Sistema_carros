# Generated by Django 5.0.6 on 2024-06-17 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='car_manufacturer', to='cars.manufacturer'),
        ),
    ]