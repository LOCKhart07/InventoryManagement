# Generated by Django 4.1.6 on 2023-02-11 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inventory_app", "0010_order_bu_code"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="bu_code",
            new_name="buCode",
        ),
    ]
