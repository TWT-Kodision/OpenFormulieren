# Generated by Django 2.2.24 on 2021-12-09 09:47

from django.db import migrations

import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_auto_20210816_1639"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="information",
            field=tinymce.models.HTMLField(
                blank=True,
                help_text="Information text to be displayed in the confirmation page and confirmation email.",
                verbose_name="information",
            ),
        ),
    ]
