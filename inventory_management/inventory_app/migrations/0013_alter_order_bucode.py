# Generated by Django 4.1.6 on 2023-02-11 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory_app", "0012_alter_order_bucode"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="buCode",
            field=models.CharField(default="0000", max_length=30),
        ),
    ]