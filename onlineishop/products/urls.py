from django.urls import path

from .views import Products, Product

urlpatterns = [
    path("products/", Products.as_view(), name="get-all-products"),
    path("products/<int:pk>/", Product.as_view(), name="get-product-detail"),
]
