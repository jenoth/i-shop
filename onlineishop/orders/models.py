from django.db import models

from onlineishop.carts.models import Cart


class Order(models.Model):
    OrderStatus = models.TextChoices("OrderStatus", "INITIATED CONFIRMED SHIPPED CANCELLED")

    delivery_date = models.DateTimeField()
    status = models.CharField(choices=OrderStatus.choices, max_length=10, default=OrderStatus.INITIATED)
    # This address is only used for this order. Otherwise, we can use the default address of the user.
    shipping_address = models.TextField(null=True)
    # Any additional details can be stored here. Eg, any reason for order cancellation.
    comments = models.TextField(null=True)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
