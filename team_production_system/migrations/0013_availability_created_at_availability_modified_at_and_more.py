# Generated by Django 4.2.6 on 2023-10-11 04:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "team_production_system",
            "0012_remove_availability_availability_constraint_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="availability",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(
                    2023, 10, 11, 4, 24, 26, 645977, tzinfo=datetime.timezone.utc
                ),
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="availability",
            name="modified_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="session",
            name="modified_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
