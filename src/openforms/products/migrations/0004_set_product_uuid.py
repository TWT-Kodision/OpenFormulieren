# Generated by Django 2.2.24 on 2021-08-16 14:35
import uuid

from django.db import migrations


def set_uuid(apps, _):
    Product = apps.get_model("products", "Product")
    for product in Product.objects.all():
        product.uuid = uuid.uuid4()
        product.save()


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_auto_20210816_1635"),
    ]

    operations = [
        migrations.RunPython(set_uuid, migrations.RunPython.noop),
    ]
