# Generated by Django 4.2.11 on 2024-03-29 05:38

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_requirement_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='location',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(), blank=True, default=list, null=True, size=None),
        ),
    ]
