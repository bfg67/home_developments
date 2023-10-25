from django import forms
from . import models
from django.core.exceptions import ValidationError
from django.forms import ModelForm


class CurrencyForm(ModelForm):
    class Meta:
        model = models.Currency
        fields = '__all__'

    def update_obj(self, pk):
        name = self.cleaned_data.get("name")
        description = self.cleaned_data.get("description")
        models.Currency.objects.filter(pk=pk).update(
            name=name,
            description=description,
        )


class OrderForm(ModelForm):
    class Meta:
        model = models.Order
        fields = '__all__'

    def update_obj(self, pk):
        user = self.cleaned_data.get("user")
        summ = self.cleaned_data.get("summ")
        order_currency = self.cleaned_data.get("order_currency")
        models.Order.objects.filter(pk=pk).update(
            user=user,
            summ=summ,
            order_currency=order_currency,
        )

