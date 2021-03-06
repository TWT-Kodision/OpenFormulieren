# Generated by Django 2.2.25 on 2021-12-31 09:54

from django.db import migrations


def limit_timout(apps, schema_editor):
    GlobalConfiguration = apps.get_model("config", "GlobalConfiguration")
    # a new system might not have the singleton
    config = GlobalConfiguration.objects.first()
    if not config:
        return

    if config.form_session_timeout > 15:
        config.form_session_timeout = 15
        config.save()


class Migration(migrations.Migration):
    dependencies = [
        ("config", "0011_auto_20211122_1628"),
    ]

    operations = [
        migrations.RunPython(limit_timout, reverse_code=migrations.RunPython.noop),
    ]
