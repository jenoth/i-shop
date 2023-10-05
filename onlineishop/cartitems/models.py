from django.core.exceptions import ValidationError
from django.db import models

from onlineishop.carts.models import Cart
from onlineishop.products.models import Product


def validate_positive(value):
    if value < 1:
        raise ValidationError(f"{value} is not an a positive number")


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[validate_positive])
    cart = models.ForeignKey(Cart, null=True, on_delete=models.SET_NULL)
