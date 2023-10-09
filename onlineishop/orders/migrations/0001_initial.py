# Generated by Django 4.2.6 on 2023-10-09 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [("carts", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("delivery_date", models.DateTimeField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("INITIATED", "Initiated"),
                            ("CONFIRMED", "Confirmed"),
                            ("SHIPPED", "Shipped"),
                            ("CANCELLED", "Cancelled"),
                        ],
                        default="INITIATED",
                        max_length=10,
                    ),
                ),
                ("shipping_address", models.TextField(blank=True, null=True)),
                ("comments", models.TextField(blank=True, null=True)),
                (
                    "cart",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="carts.cart"
                    ),
                ),
            ],
            options={"db_table": "order", "db_table_comment": "Orders of customer"},
        )
    ]