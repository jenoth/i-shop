from rest_framework import generics
from rest_framework.response import Response

from .models import CartItem as CartItemModel
from .serializers import CartItemSerializer
from ..carts.models import Cart as CartModel
from ..products.models import Product as ProductModel


class CartItemAddView(generics.GenericAPIView):
    queryset = CartItemModel.objects.all()
    serializer_class = CartItemSerializer

    def post(self, request, cart_id):
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
        cart_items_query_set = CartItemModel.objects.all()
        cart_items_serializer = self.serializer_class(cart_items_query_set, many=True)

        # Perform bulk updating
        filter_condition = {"cart": cart_id, "product__in": products_to_update}
        products_to_bulk_update = CartItemModel.objects.filter(**filter_condition)

        for item in products_to_bulk_update:
            item.quantity = request_data_dict[item.product_id]
        CartItemModel.objects.bulk_update(products_to_bulk_update, ["quantity"])

        return Response(
            {
                "status": "success",
                "status_code": 200,
                "items": cart_items_serializer.data,
            }
        )
