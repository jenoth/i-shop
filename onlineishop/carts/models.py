from django.db import models

from onlineishop.customers.models import Customer
from onlineishop.products.models import Product


class Cart(models.Model):
    """It is a temporary storage of an ordering process. This records should be removed once the
    customer finishes his order or if he or she ends the session or logout."""

    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, verbose_name="list of products")
    quantity = models.IntegerField()

    def __str__(self):
        return f"Cart of customer, {self.customer}"
