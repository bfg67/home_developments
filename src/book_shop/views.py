from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model

User = get_user_model()

from . import models, forms


def currency_detail(request, pk):
    obj = models.Currency.objects.get(pk=pk)
    context = {"obj": obj, "verb": "detail"}
    return render(
        request,
        template_name="book_shop/currency_detail.html",
        context=context
    )


def currency_list(request):
    obj_list = models.Currency.objects.all()
    context = {"obj_list": obj_list, "verb": "list"}
    return render(
        request,
        template_name="book_shop/currency_list.html",
        context=context
    )


def currency_create(request):
    template_name = "book_shop/currency_create.html"
    if request.method == "GET":
        form = forms.CurrencyForm()
        context = {"verb": "create", "form": form}
    elif request.method == "POST":
        form = forms.CurrencyForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(f"/book_shop/currency/{obj.pk}")
        else:
            context = {"verb": "create", "form": form}

    else:
        raise Exception("WRONG METHOD")
    return render(
            request,
            template_name=template_name,
            context=context
        )


def currency_update(request, pk):
    if request.method == "GET":
        template_name = "book_shop/currency_update.html"
        obj = models.Currency.objects.get(pk=pk)
        form = forms.CurrencyForm({
            "name": obj.name,
            "description": obj.description,
        })
        context = {"obj": obj, "verb": "update", "form": form}
    elif request.method == "POST":
        form = forms.CurrencyForm(request.POST)
        if form.is_valid():
            form.update_obj(pk)
            return HttpResponseRedirect(f"/book_shop/currency/{pk}")
    else:
        raise Exception("WRONG METHOD")
    return render(
        request,
        template_name=template_name,
        context=context,
    )


def order_detail(request, pk):
    obj = models.Order.objects.get(pk=pk)
    context = {"obj": obj, "verb": "detail"}
    return render(
        request,
        template_name="book_shop/order_detail.html",
        context=context
    )


def order_list(request):
    obj_list = models.Order.objects.all()
    context = {"obj_list": obj_list, "verb": "list"}
    return render(
        request,
        template_name="book_shop/order_list.html",
        context=context
    )


def order_create(request):
    template_name = "book_shop/order_create.html"
    if request.method == "GET":
        form = forms.OrderForm()
        context = {"verb": "create", "form": form}
    elif request.method == "POST":
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            obj = form.save()
        return HttpResponseRedirect(f"/book_shop/order/{obj.pk}")
    else:
        raise Exception("WRONG METHOD")
    return render(
            request,
            template_name=template_name,
            context=context
        )


def order_update(request, pk):
    if request.method == "GET":
        template_name = "book_shop/order_update.html"
        obj = models.Order.objects.get(pk=pk)
        all_users = User.objects.all()
        all_currency = models.Currency.objects.all()
        context = {
            "obj": obj,
            "verb": "update",
            "all_users": all_users,
            "all_currency": all_currency,
        }
    elif request.method == "POST":
        user = request.POST.get("user")
        summ = request.POST.get("summ")
        order_currency = request.POST.get("order_currency")
        print(user, summ, order_currency)
        obj = models.Order.objects.update(
            user=User.objects.get(pk=int(user)),
            summ=summ,
            order_currency=models.Currency.objects.get(pk=order_currency),
        )
        return HttpResponseRedirect(f"/book_shop/order/{obj}")

    else:
        raise Exception("WRONG METHOD")
    return render(
            request,
            template_name=template_name,
            context=context
        )
