from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Currency(models.Model):
    name = models.CharField(
        verbose_name="Currency name IS03",
        max_length=3
    )
    description = models.TextField(
        verbose_name="Currency description",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return f"/book_shop/currency/{self.pk}/"


class Order(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Customer",
        on_delete=models.PROTECT
    )
    summ = models.DecimalField(
        verbose_name="Order summ",
        max_digits=6,
        decimal_places=2
    )
    order_currency = models.ForeignKey(
    "book_shop.Currency",
        verbose_name="Currency",
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f"Order for User {self.user.username} - {self.summ} {self.order_currency.name}"

    def get_absolute_url(self):
        return f"/book_shop/order/{self.pk}/"


