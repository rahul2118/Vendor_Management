from django.urls import path
from .views import (
    vendor_list_create,
    vendor_detail,
    purchase_order_list_create,
    purchase_order_detail,
    vendor_performance
)

urlpatterns = [
    path('vendors/', vendor_list_create, name='vendor-list-create'),
    path('vendors/<int:vendor_id>/', vendor_detail, name='vendor-detail'),
    path('purchase_orders/', purchase_order_list_create, name='purchase-order-list-create'),
    path('purchase_orders/<int:po_id>/', purchase_order_detail, name='purchase-order-detail'),
    path('vendors/<int:vendor_id>/performance/', vendor_performance, name='vendor-performance'),
]