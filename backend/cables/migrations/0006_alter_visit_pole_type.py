# Generated by Django 4.0.1 on 2022-01-28 15:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sinp_nomenclatures", "0002_alter_source_unique_together"),
        ("cables", "0005_remove_visit_pole_type_visit_pole_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="visit",
            name="pole_type",
            field=models.ForeignKey(
                help_text="Type of pole",
                limit_choices_to={"type__mnemonic": "pole_type"},
                on_delete=django.db.models.deletion.PROTECT,
                related_name="visit_pole_type",
                to="sinp_nomenclatures.item",
                verbose_name="Type of pole",
            ),
        ),
    ]
