# Generated by Django 3.2.12 on 2022-03-18 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0020_migrate_kvk_prefill"),
    ]

    operations = [
        migrations.AddField(
            model_name="form",
            name="auto_login_authentication_backend",
            field=models.CharField(
                blank=True, max_length=100, verbose_name="automatic login"
            ),
        ),
    ]
