from django.shortcuts import render
from django.http import  HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.views.generic import DeleteView
from django.views.generic import DetailView, UpdateView, CreateView, ListView

User = get_user_model()

from . import models, forms


class CurrencyList(ListView):
    template_name = "book_shop/currency_list"
    model = models.Currency


class OrderCreate(CreateView):
    template_name = "book_shop/order_create.html"
    model = models.Order
    form_class = forms.OrderForm


class CurrencyCreate(CreateView):
    template_name = "book_shop/currency_create.html"
    model = models.Currency
    form_class = forms.CurrencyForm


class CurrencyUpdate(UpdateView):
    template_name = "book_shop/currency_update.html"
    model = models.Currency
    fields = [
        'name',
        'description',
    ]


class OrderDetail(DetailView):
    template_name = "book_shop/order_detail.html"
    model = models.Order

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "Detail"
        return context


class CurrencyDetail(DetailView):
    template_name = "book_shop/currency_detail.html"
    model = models.Currency

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "Detail"
        return context


class OrderUpdate(UpdateView):
    template_name = "book_shop/order_update.html"
    model = models.Order
    form_class = forms.OrderForm


class OrderList(ListView):
    template_name = "book_shop/order_list.html"
    model = models.Order


class OrderDelete(DeleteView):
    template_name = "book_shop/order_delete.html"
    model = models.Order
    success_url = "/book_shop/order/"

class CurrencyDelete(DeleteView):
    template_name = "book_shop/currency_delete.html"
    model = models.Currency
    success_url = "/book_shop/currency/"





