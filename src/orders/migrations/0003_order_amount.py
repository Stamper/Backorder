# Generated by Django 4.1 on 2022-09-02 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_order_invoice"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="amount",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
