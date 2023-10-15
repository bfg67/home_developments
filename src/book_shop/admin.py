from django.contrib import admin
from . import models


class CurrencyAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'description'
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'user',
        'summ',
        'order_currency',
    ]


admin.site.register(models.Currency, CurrencyAdmin)
admin.site.register(models.Order, OrderAdmin)
