from django.urls import path

from .views import CustomerListCreateView, CustomerDetailView
from ..cartitems.views import CartItemAddView

urlpatterns = [
    path("customers/", CustomerListCreateView.as_view(), name="customer-list-create"),
    path("customers/<int:pk>/", CustomerDetailView.as_view(), name="customer-detail"),
    path("customers/<int:customer_id>/carts/<int:cart_id>/products/", CartItemAddView.as_view(), name="customer-cart-cud"),
]
