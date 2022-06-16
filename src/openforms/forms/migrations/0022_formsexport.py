# Generated by Django 3.2.13 on 2022-04-20 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import openforms.utils.files
import privates.fields
import privates.storages
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("forms", "0021_form_auto_login_authentication_backend"),
    ]

    operations = [
        migrations.CreateModel(
            name="FormsExport",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, unique=True, verbose_name="UUID"
                    ),
                ),
                (
                    "export_content",
                    privates.fields.PrivateMediaFileField(
                        help_text="Zip file containing all the exported forms.",
                        storage=privates.storages.PrivateMediaFileSystemStorage(),
                        upload_to="exports/%Y/%m/%d",
                        verbose_name="export content",
                    ),
                ),
                (
                    "datetime_requested",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="The date and time on which the bulk export was requested.",
                        verbose_name="date time requested",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="The user that requested the download.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "verbose_name": "forms export",
                "verbose_name_plural": "forms exports",
            },
            bases=(openforms.utils.files.DeleteFileFieldFilesMixin, models.Model),
        ),
    ]