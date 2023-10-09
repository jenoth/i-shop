from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics

from .models import Customer
from .serializers import CustomerSerializer


class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @swagger_auto_schema(auto_schema=None)
    def patch(self, request, *args, **kwargs):
        return super().patch(self, request, *args, **kwargs)
