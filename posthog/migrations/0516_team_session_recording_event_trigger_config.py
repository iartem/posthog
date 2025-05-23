# Generated by Django 4.2.15 on 2024-11-13 14:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("posthog", "0515_grouptypemapping_project_non_null")]

    operations = [
        migrations.AddField(
            model_name="team",
            name="session_recording_event_trigger_config",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.TextField(blank=True, null=True), blank=True, default=list, null=True, size=None
            ),
        ),
    ]
