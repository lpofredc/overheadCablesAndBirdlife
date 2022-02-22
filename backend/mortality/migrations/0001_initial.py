# Generated by Django 4.0.1 on 2022-02-03 07:20

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("media", "0001_initial"),
        ("sinp_nomenclatures", "0002_alter_source_unique_together"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mortality",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp_create", models.DateTimeField(auto_now_add=True)),
                ("timestamp_update", models.DateTimeField(auto_now=True)),
                (
                    "date",
                    models.DateField(
                        default=django.utils.timezone.now,
                        verbose_name="Mortality observation date",
                    ),
                ),
                (
                    "nb_death",
                    models.IntegerField(
                        default=1, verbose_name="Number found dead"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        help_text="Author of the mortality observation",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="mortality_author",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Author of the mortality observation",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "data_source",
                    models.ForeignKey(
                        blank=True,
                        help_text="Mortality data source",
                        limit_choices_to={"type__mnemonic": "organism"},
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="mortality_data_source",
                        to="sinp_nomenclatures.nomenclature",
                        verbose_name="Mortality data source",
                    ),
                ),
                (
                    "death_cause",
                    models.ForeignKey(
                        help_text="Cause of death",
                        limit_choices_to={"type__mnemonic": "cause_of_death"},
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="mortality_cod",
                        to="sinp_nomenclatures.nomenclature",
                        verbose_name="Cause of death",
                    ),
                ),
                (
                    "media",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Media related to the mortality case",
                        related_name="mortality_media",
                        to="media.Media",
                        verbose_name="Media related to the mortality case",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
