from django.db import models


class Order(models.Model):
    OrderStatus = models.TextChoices("OrderStatus", "INITIATED CONFIRMED SHIPPED CANCELLED")

    delivery_date = models.DateTimeField()
    status = models.CharField(choices=OrderStatus.choices, max_length=10, default=OrderStatus.CONFIRMED)
    # This address is only used for this order. Otherwise, we can use the default address of the user.
    shipping_address = models.TextField(null=True, blank=True)
    # Any additional details can be stored here. Eg, any reason for order cancellation.
    comments = models.TextField(null=True, blank=True)
