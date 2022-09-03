from datetime import datetime
from typing import Optional
from ninja import Schema, ModelSchema


class ProductNew(Schema):
    title: str
    description: Optional[str]
    price: float


class ProductUpdate(Schema):
    title: Optional[str]
    description: Optional[str]
    price: Optional[float]


class ProductResponse(Schema):
    id: int
    title: str
    price: float
    created: datetime
    discount: float


class OrderResponse(Schema):
    id: int
    product: ProductResponse
    amount: float
    created: datetime
    done: bool


class InvoiceResponse(Schema):
    id: int
    order: OrderResponse
    created: datetime
    paid: bool
