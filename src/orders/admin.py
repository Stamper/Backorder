from django.contrib import admin

from orders.models import Product, Order, Invoice


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "price",
        "discount",
        "created",
    )


@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ("id", "created", "product", "amount", "done")


@admin.register(Invoice)
class InvoicesAdmin(admin.ModelAdmin):
    list_display = ("id", "created", "order", "paid")
