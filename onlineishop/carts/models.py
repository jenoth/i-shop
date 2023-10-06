from django.db import models

from onlineishop.customers.models import Customer
from onlineishop.orders.models import Order


class Cart(models.Model):
    """It is a temporary storage of an ordering process. This records should be removed once the
    customer finishes his order or if he or she ends the session or logout."""

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.OneToOneField(Order, null=True, blank=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}, Shopping cart of {self.customer}"
