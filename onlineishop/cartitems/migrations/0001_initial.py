# Generated by Django 4.2.6 on 2023-10-09 04:18

from django.db import migrations, models
import onlineishop.cartitems.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CartItem",
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
                (
                    "quantity",
                    models.IntegerField(
                        default=1,
                        validators=[onlineishop.cartitems.models.validate_positive],
                    ),
                ),
            ],
            options={"db_table_comment": "Ordered(cart) items of customer"},
        )
    ]
