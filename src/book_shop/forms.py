from django import forms
from . import models
from django.core.exceptions import ValidationError


def my_validator(field):
    if field == "xxx":
       raise ValidationError("Eror")


class CurrencyForm(forms.Form):
    name = forms.CharField(
        max_length=3,
        required=True,
        validators=[my_validator]
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea()
    )

    def save_obj(self):
        name = self.cleaned_data.get("name")
        description = self.cleaned_data.get("description")
        obj = models.Currency.objects.create(
            name=name,
            description=description,
        )
        return obj


    def update_obj(self):
        name = self.cleaned_data.get("name")
        description = self.cleaned_data.get("description")
        obj_pk = models.Currency.objects.update(
            name=name,
            description=description,
        )
        return obj_pk


