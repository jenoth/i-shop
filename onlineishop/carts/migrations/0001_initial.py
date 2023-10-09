# Generated by Django 4.2.6 on 2023-10-09 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0001_initial"),
        ("customers", "0001_initial"),
        ("cartitems", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "cartitems",
                    models.ManyToManyField(
                        through="cartitems.CartItem", to="products.product"
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customers.customer",
                    ),
                ),
            ],
            options={"db_table": "cart"},
        )
    ]
