# Generated by Django 4.0.1 on 2022-01-21 10:56

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cables", "0010_alter_equipment_equipment_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipment",
            name="equipment_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 1, 21, 11, 56, 4, 853404),
                editable=False,
            ),
        ),
    ]
