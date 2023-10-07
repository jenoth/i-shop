from django.db import models

from onlineishop.cartitems.models import CartItem
from onlineishop.customers.models import Customer
from onlineishop.products.models import Product


class Cart(models.Model):
    """It is a temporary storage of an ordering process. This records should be removed or marked as non-active once the
    customer finishes his order or if he or she ends the session or logout."""

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cartitems = models.ManyToManyField(Product, through=CartItem)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "cart"

    def __str__(self):
        return f"{self.id}, Shopping cart of {self.customer}"

    def save(self, *args, **kwargs):
        """Overriding the existing save method which is triggered when create or update the record."""
        if carts := self.is_active and Cart.objects.filter(customer=self.customer, is_active=True):
            if (carts.count() > 1) or (self.pk is None) or (self.id != carts[0].id):
                raise ValueError("Customer has active cart(s) which is a db integrity error according to our design")
        super().save(*args, **kwargs)
