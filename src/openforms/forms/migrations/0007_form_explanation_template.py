# Generated by Django 2.2.24 on 2021-12-06 08:41

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0006_formpricelogic"),
    ]

    operations = [
        migrations.AddField(
            model_name="form",
            name="explanation_template",
            field=tinymce.models.HTMLField(
                blank=True,
                help_text="Content that will be shown on the start page of the form, below the title and above the log in text.",
                verbose_name="explanation template",
            ),
        ),
    ]
