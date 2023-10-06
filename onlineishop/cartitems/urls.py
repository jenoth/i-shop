from django.urls import path

from .views import CartItemAddView

urlpatterns = [
    path("carts/<int:cart_id>/cartitems/", CartItemAddView.as_view(), name="get-product-detail"),
]
