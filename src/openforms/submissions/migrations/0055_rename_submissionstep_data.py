# Generated by Django 3.2.13 on 2022-06-01 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("submissions", "0054_submissionvaluevariable"),
    ]

    operations = [
        migrations.RenameField(
            model_name="submissionstep",
            old_name="data",
            new_name="_data",
        ),
    ]
