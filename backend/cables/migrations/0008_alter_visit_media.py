# Generated by Django 4.0.1 on 2022-01-28 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("media", "0001_initial"),
        ("cables", "0007_alter_visit_condition_alter_visit_media_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="visit",
            name="media",
            field=models.ManyToManyField(
                blank=True,
                help_text="Media attached with this visit",
                related_name="visit_media",
                to="media.Media",
                verbose_name="Media attached with this visit",
            ),
        ),
    ]
