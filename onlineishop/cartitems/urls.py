from django.urls import path

from .views import CartItemCreateUpdateDeleteView

urlpatterns = [
    path("carts/<int:cart_id>/cartitems/", CartItemCreateUpdateDeleteView.as_view()),
]
