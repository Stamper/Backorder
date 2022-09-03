from typing import List

from ninja import Router
from django.shortcuts import get_object_or_404

from backorder.schemas import ProductResponse, ProductNew, ProductUpdate
from orders.models import Product

router = Router()


@router.get("/", response=List[ProductResponse])
def get_products(request):
    return Product.objects.all()


@router.get("/{product_id}", response=ProductResponse)
def get_product(request, product_id: int):
    return get_object_or_404(Product, id=product_id)


@router.post("/", response=ProductResponse)
def create_product(request, payload: ProductNew):
    return Product.objects.create(**payload.__dict__)


@router.patch("/{product_id}", response=ProductResponse)
def update_product(request, product_id: int, payload: ProductUpdate):
    product = get_object_or_404(Product, id=product_id)
    for k, v in payload.__dict__.items():
        if v:
            setattr(product, k, v)
    product.save()
    return product


@router.delete("/{product_id}")
def delete_product(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
