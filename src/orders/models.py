from decimal import Decimal

from django.conf import settings
from django.utils import timezone
from django.db import models
from django_extensions.db.models import TitleDescriptionModel, TimeStampedModel


class Product(TitleDescriptionModel, TimeStampedModel):
    price = models.DecimalField(max_digits=6, decimal_places=2)

    @property
    def discount(self):
        diff = timezone.now() - self.created
        if diff.days > settings.PRODUCT_EXP:
            return round(self.price * Decimal.from_float(settings.PRODUCT_DISCOUNT), 2)

        return 0

    def __str__(self):
        return self.title


class Order(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.SmallIntegerField(default=0)
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def mark_done(self):
        self.status = 1
        self.save()

    def save(self):
        self.amount = self.product.price - self.product.discount
        super().save()

    @property
    def done(self):
        return bool(self.status)

    def __str__(self):
        return f"Order #{self.id} {self.created}"


class Invoice(TimeStampedModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.SmallIntegerField(default=0)

    def mark_paid(self):
        self.status = 1
        self.save()

    @property
    def paid(self):
        return bool(self.status)
