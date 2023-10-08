import decimal

from rest_framework import generics
from rest_framework.response import Response

from .models import CartItem as CartItemModel
from .serializers import CartItemsResponseSerializer
from ..carts.models import Cart as CartModel
from ..products.models import Product as ProductModel


class CartItemAddView(generics.GenericAPIView):
    def get_queryset(self, cart_id):
        return CartItemModel.objects.filter(cart_id=cart_id)

    def post(self, request, customer_id, cart_id):
        """Single API to handle all bulk insertion, updating and deletion of cart items"""
        # if existing products(db) are not in request data, DELETE all. removed product
        # if existing products(db) are available in request data, UPDATE all. existing product. to be updated
        # if products in request data which are not in existing(db) , CREATE all. non existing product. to be created

        # to have unique products with requested quantity
        request_data_dict = {data["product_id"]: data["quantity"] for data in request.data}

        existing_product_ids = set([item.product_id for item in CartItemModel.objects.filter(cart=cart_id)])
        current_product_ids = set(request_data_dict)

        products_to_remove = existing_product_ids - current_product_ids
        products_to_insert = current_product_ids - existing_product_ids
        products_to_update = current_product_ids & existing_product_ids

        # Perform bulk deletion
        filter_condition = {"cart": cart_id, "product__in": products_to_remove}
        deleted_count, _ = CartItemModel.objects.filter(**filter_condition).delete()

        cart_object = CartModel.objects.get(pk=cart_id)
        objects_to_insert = [
            CartItemModel(cart=cart_object, product=ProductModel.objects.get(pk=k), quantity=v)
            for k, v in request_data_dict.items()
            if k in products_to_insert
        ]

        # Perform bulk insertion
        _ = CartItemModel.objects.bulk_create(objects_to_insert)

        # Perform bulk updating
        filter_condition = {"cart": cart_id, "product__in": products_to_update}
        products_to_bulk_update = CartItemModel.objects.filter(**filter_condition)

        for item in products_to_bulk_update:
            item.quantity = request_data_dict[item.product_id]
        CartItemModel.objects.bulk_update(products_to_bulk_update, ["quantity"])

        # generating the response
        response_products = []
        total_price_of_cart = decimal.Decimal()
        for cart_item in self.get_queryset(self.kwargs["cart_id"]):
            no_of_ordered_product = cart_item.quantity
            unit_price_of_ordered_product = cart_item.product.price
            total_price_of_ordered_product = unit_price_of_ordered_product * no_of_ordered_product
            response_products.append(
                {
                    "id": cart_item.product.id,
                    "name": cart_item.product.name,
                    "unit_price": unit_price_of_ordered_product,
                    "quantity": no_of_ordered_product,
                    "total_price": total_price_of_ordered_product,
                }
            )
            total_price_of_cart += total_price_of_ordered_product

        return Response(
            {
                "cart_total": str(total_price_of_cart),
                "products": CartItemsResponseSerializer(response_products, many=True).data,
            }
        )
