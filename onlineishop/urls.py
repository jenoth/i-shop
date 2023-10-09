"""
URL configuration for onlineishop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from onlineishop.cartitems.views import CartItemCRUDView

schema_view = get_schema_view(
    openapi.Info(
        title="I-SHOP OpenAPI Specification (OAS)",
        default_version="v1",
        description="Open API(Swagger UI) definitions for I-SHOP",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/v1/",
        include(
            [
                path("", include("onlineishop.customers.urls")),
                path("", include("onlineishop.products.urls")),
                path("", include("onlineishop.carts.urls")),
                # path("", include("onlineishop.cartitems.urls")),
                # path("", include("onlineishop.orders.urls")),
                path(
                    "customers/<int:customer_id>/carts/<int:cart_id>/products/",
                    CartItemCRUDView.as_view(),
                ),
            ]
        ),
    ),
    path("ui/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
