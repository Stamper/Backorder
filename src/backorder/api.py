from ninja import NinjaAPI
from backorder.routers.products import router as products_router
from backorder.routers.orders import router as orders_router
from backorder.routers.invoices import router as invoices_router

api = NinjaAPI()

api.add_router("/products/", products_router, tags=["Products"])
api.add_router("/orders/", orders_router, tags=["Orders"])
api.add_router("/invoices/", invoices_router, tags=["Invoices"])
