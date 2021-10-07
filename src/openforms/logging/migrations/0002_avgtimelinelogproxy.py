# Generated by Django 2.2.24 on 2021-09-28 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("logging", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AVGTimelineLogProxy",
            fields=[],
            options={
                "verbose_name": "avg timeline log entry",
                "verbose_name_plural": "avg timeline log entries",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("logging.timelinelogproxy",),
        ),
    ]
