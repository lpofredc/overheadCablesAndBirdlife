# Generated by Django 4.0.1 on 2022-03-01 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sinp_nomenclatures", "0002_alter_source_unique_together"),
        ("cables", "0003_alter_diagnosis_condition_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="diagnosis",
            name="pole_type",
            field=models.ManyToManyField(
                help_text="Type of pole",
                limit_choices_to={"type__mnemonic": "pole_type"},
                related_name="visit_pole_type",
                to="sinp_nomenclatures.Item",
                verbose_name="Type of pole",
            ),
        ),
    ]