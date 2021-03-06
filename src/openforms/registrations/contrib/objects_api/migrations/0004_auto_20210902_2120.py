# Generated by Django 2.2.24 on 2021-09-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registrations_objects_api", "0003_auto_20210831_1310"),
    ]

    operations = [
        migrations.AlterField(
            model_name="objectsapiconfig",
            name="productaanvraag_type",
            field=models.CharField(
                blank=True,
                help_text="Description of the 'ProductAanvraag' type. This value is saved in the 'type' attribute of the 'ProductAanvraag'.",
                max_length=255,
                verbose_name="Productaanvraag type",
            ),
        ),
    ]
