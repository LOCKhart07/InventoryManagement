# Generated by Django 4.1.6 on 2023-02-11 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inventory_app", "0008_delete_orderhistory"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Admin",
        ),
    ]
