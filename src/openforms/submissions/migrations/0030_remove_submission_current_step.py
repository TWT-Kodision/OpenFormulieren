# Generated by Django 2.2.24 on 2021-09-08 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("submissions", "0029_auto_20210907_1803"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="submission",
            name="current_step",
        ),
    ]
