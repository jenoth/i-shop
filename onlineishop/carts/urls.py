from django.urls import path

from .views import CartListCreateView, CartRetrieveUpdateView, CartDeleteView

urlpatterns = [
    path("carts/", CartListCreateView.as_view(), name="cart-list-create"),
    path("carts/<int:pk>/", CartRetrieveUpdateView.as_view(), name="cart-detail"),
    path("carts/<int:pk>/delete", CartDeleteView.as_view(), name="cart-delete"),
]
