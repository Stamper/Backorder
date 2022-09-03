from typing import List

from ninja import Router
from django.shortcuts import get_object_or_404

from backorder.schemas import InvoiceResponse
from orders.models import Order, Invoice

router = Router()


@router.post("/{order_id}", response={200: InvoiceResponse, 400: str})
def create_invoice(request, order_id: int):
    order = get_object_or_404(Order, pk=order_id)
    if not order.done:
        return 400, "Order is not completed"
    return Invoice.objects.create(order=order)


@router.get("/", response=List[InvoiceResponse])
def get_invoices(request):
    return Invoice.objects.all()


@router.post("/{invoice_id}/paid", response=InvoiceResponse)
def mark_order_done(request, invoice_id: int):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    invoice.mark_paid()
    return invoice
