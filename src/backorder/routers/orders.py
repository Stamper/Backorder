from typing import List
from datetime import datetime

from ninja import Router
from django.shortcuts import get_object_or_404

from backorder.schemas import OrderResponse
from orders.models import Product, Order

router = Router()


@router.post("/{product_id}", response=OrderResponse)
def create_order(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    new_order = Order(product=product)
    new_order.save()
    return new_order


@router.get(
    "/",
    response=List[OrderResponse],
    description="Start/End date in format '2022-01-20T10:30:00'",
)
def get_orders(request, start: datetime = None, end: datetime = None):
    query = Order.objects
    if start:
        query = query.filter(created__gt=start)
    if end:
        query = query.filter(created__lt=end)
    return query.all()


@router.post("/{order_id}/done", response=OrderResponse)
def mark_order_done(request, order_id: int):
    order = get_object_or_404(Order, id=order_id)
    order.mark_done()
    return order
