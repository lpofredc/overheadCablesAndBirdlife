# Generated by Django 4.0.1 on 2022-02-16 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mortality", "0007_mortality_infrstr"),
    ]

    operations = [
        migrations.RenameField(
            model_name="mortality",
            old_name="geom",
            new_name="mort_geom",
        ),
    ]
