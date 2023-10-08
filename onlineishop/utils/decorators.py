from functools import wraps

from rest_framework.response import Response

from onlineishop.carts.models import Cart


def active_cart_validator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if Cart.objects.filter(id=kwargs["cart_id"], is_active=True).exists():
            return func(*args, **kwargs)

        error_response_data = {
            "type": "/errors/invalid-cart-id",
            "title": "Incorrect active cart id",
            "status": 404,
            "detail": "There is no any active carts",
            "instance": "trace_id",
        }
        return Response(data=error_response_data, status=404)

    return wrapper
