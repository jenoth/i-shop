import math

from rest_framework import generics
from rest_framework.response import Response

from .models import Product as ProductModel
from .serializers import ProductSerializer


class Product(generics.RetrieveAPIView):
    """Default RetrieveAPIView to get a product for a given product id"""

    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


class Products(generics.GenericAPIView):
    """GenericAPIView for getting all the products by providing pagination and search query"""

    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        """GET controller for getting all the filtered and paginated products"""
        # if we do not provide page query parameter then we will get None. But, we provide 1 as default value.
        # If we provide page query parameter without a value then we will get empty string
        # page or limit query params must be a natural number(positive integer)
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        products_query_set = ProductModel.objects.all()
        no_of_carts = products_query_set.count()
        if search_param:
            products_query_set = products_query_set.filter(name__icontains=search_param)
        serializer = self.serializer_class(products_query_set[start_num:end_num], many=True)
        return Response(
            {
                "status": "success",
                "status_code": 200,
                "total_products": no_of_carts,
                "current_page": page_num,
                "last_page": math.ceil(no_of_carts / limit_num),
                "products": serializer.data,
            }
        )
