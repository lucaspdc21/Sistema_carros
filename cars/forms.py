from django import forms

from cars.models import Manufacturer

class NewCarForm(forms.Form):
    model = forms.CharField(max_length=150)
    manufacturer = forms.ModelChoiceField(Manufacturer.objects.all())
    model_year = forms.IntegerField()
    factory_year = forms.IntegerField()
    value = forms.IntegerField()
    plate = forms.CharField()
    photo = forms.ImageField()

