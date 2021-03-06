# Generated by Django 2.2.27 on 2022-02-07 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("submissions", "0047_submission_prefill_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="temporaryfileupload",
            name="file_size",
            field=models.PositiveIntegerField(
                default=0,
                help_text="Size in bytes of the uploaded file.",
                verbose_name="file size",
            ),
        ),
    ]
