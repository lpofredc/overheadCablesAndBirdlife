# Generated by Django 4.0.1 on 2022-01-13 14:10

import datetime
import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("media", "0001_initial"),
        ("sinp_nomenclatures", "0002_alter_source_unique_together"),
        ("cables", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Observation",
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
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        unique=True,
                        verbose_name="unique Id",
                    ),
                ),
                (
                    "inventory_date",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2022, 1, 13, 15, 10, 15, 638612
                        ),
                        editable=False,
                        verbose_name="Inventory date",
                    ),
                ),
                (
                    "observation_date",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2022, 1, 13, 15, 10, 15, 638627
                        ),
                        verbose_name="Observation date",
                    ),
                ),
                (
                    "observation",
                    models.TextField(
                        blank=True, null=True, verbose_name="Observation"
                    ),
                ),
                (
                    "neutralized",
                    models.BooleanField(
                        default=False, verbose_name="Neutralized"
                    ),
                ),
                (
                    "isolation_advice",
                    models.BooleanField(
                        blank=True, null=True, verbose_name="Isolation"
                    ),
                ),
                (
                    "dissuasion_advice",
                    models.BooleanField(
                        blank=True, null=True, verbose_name="Dissuasion"
                    ),
                ),
                (
                    "attraction_advice",
                    models.BooleanField(
                        blank=True, null=True, verbose_name="Attraction"
                    ),
                ),
                (
                    "condition",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        help_text="Pole condition",
                        limit_choices_to={
                            "type__mnemonic": "infrastr_condition"
                        },
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="pole_condition",
                        to="sinp_nomenclatures.item",
                        verbose_name="Pole condition",
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
                    "pictures",
                    models.ManyToManyField(
                        help_text="Segment attached with this observation",
                        related_name="observation_pictures",
                        to="media.Picture",
                        verbose_name="Segment attached with this observation",
                    ),
                ),
                (
                    "pole",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        help_text="Pole attached with this observation",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="observation_pole",
                        to="cables.pole",
                        verbose_name="Pole attached with this observation",
                    ),
                ),
                (
                    "pole_attractivity",
                    models.ForeignKey(
                        help_text="Attractivity level of risk",
                        limit_choices_to={"type__mnemonic": "risk_level"},
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="pole_attractivity",
                        to="sinp_nomenclatures.item",
                        verbose_name="Attractivity level of risk",
                    ),
                ),
                (
                    "pole_dangerousness",
                    models.ForeignKey(
                        help_text="dangerousness level of risk",
                        limit_choices_to={"type__mnemonic": "risk_level"},
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="pole_dangerousness",
                        to="sinp_nomenclatures.item",
                        verbose_name="dangerousness level of risk",
                    ),
                ),
                (
                    "pole_type_primary",
                    models.ForeignKey(
                        help_text="Primary pole type",
                        limit_choices_to={"type__mnemonic": "pole_type"},
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="pole_type_primary",
                        to="sinp_nomenclatures.item",
                        verbose_name="Primary pole type",
                    ),
                ),
                (
                    "pole_type_secondary",
                    models.ForeignKey(
                        help_text="Secondary pole type",
                        limit_choices_to={"type__mnemonic": "pole_type"},
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="pole_type_secondary",
                        to="sinp_nomenclatures.item",
                        verbose_name="Secondary pole type",
                    ),
                ),
                (
                    "segment",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        help_text="Segment attached with this observation",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="observation_segment",
                        to="cables.segment",
                        verbose_name="Segment attached with this observation",
                    ),
                ),
                (
                    "segt_build_integr_risk",
                    models.ForeignKey(
                        help_text="Building integration level of risk",
                        limit_choices_to={"type__mnemonic": "risk_level"},
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="segment_building_integration_risk",
                        to="sinp_nomenclatures.item",
                        verbose_name="Building integration level of risk",
                    ),
                ),
                (
                    "segt_moving_risk",
                    models.ForeignKey(
                        help_text="moving level of risk",
                        limit_choices_to={"type__mnemonic": "risk_level"},
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="segment_moving_risk",
                        to="sinp_nomenclatures.item",
                        verbose_name="moving level of risk",
                    ),
                ),
                (
                    "sgmt_topo_integr_risk",
                    models.ForeignKey(
                        help_text="Topological level of risk",
                        limit_choices_to={"type__mnemonic": "risk_level"},
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="segment_topological_integration_risk",
                        to="sinp_nomenclatures.item",
                        verbose_name="topological level of risk",
                    ),
                ),
                (
                    "sgmt_veget_integr_risk",
                    models.ForeignKey(
                        help_text="vegetation level of risk",
                        limit_choices_to={"type__mnemonic": "risk_level"},
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="segment_vegetation_risk",
                        to="sinp_nomenclatures.item",
                        verbose_name="vegetation level of risk",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Equipment",
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
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        unique=True,
                        verbose_name="unique Id",
                    ),
                ),
                (
                    "equipment_date",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2022, 1, 13, 15, 10, 15, 640136
                        ),
                        editable=False,
                    ),
                ),
                (
                    "installed",
                    models.BooleanField(
                        blank=True, null=True, verbose_name="Installed"
                    ),
                ),
                (
                    "pole_nb_equipments",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        verbose_name="Number of eqipments",
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
                    "pictures",
                    models.ManyToManyField(
                        help_text="Segment attached with this observation",
                        related_name="equipment_pictures",
                        to="media.Picture",
                        verbose_name="Segment attached with this observation",
                    ),
                ),
                (
                    "pole",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        help_text="Pole the equipment is installed on",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="equipment_pole",
                        to="cables.pole",
                        verbose_name="Pole the equipment is installed on",
                    ),
                ),
                (
                    "pole_eqmt_type",
                    models.ForeignKey(
                        help_text="Type of equipment for pole",
                        limit_choices_to={"type__mnemonic": "pole_equipment"},
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="equipment_pole_eqmt_type",
                        to="sinp_nomenclatures.item",
                        verbose_name="Type of equipment for pole",
                    ),
                ),
                (
                    "segment",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        help_text="Segment the equipment is installed on",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="equipment_segment",
                        to="cables.segment",
                        verbose_name="Segment the equipment is installed on",
                    ),
                ),
                (
                    "sgmt_eqmt_type",
                    models.ForeignKey(
                        help_text="Type of equipment for segment",
                        limit_choices_to={"type__mnemonic": "pole_equipment"},
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="equipment_sgmt_eqmt_type",
                        to="sinp_nomenclatures.item",
                        verbose_name="Type of equipment for segment",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="observation",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(
                        ("pole__isnull", False), ("segment__isnull", True)
                    ),
                    models.Q(
                        ("pole__isnull", True), ("segment__isnull", False)
                    ),
                    _connector="OR",
                ),
                name="cables_observation_only_one_of_both_field_not_null_constraint",
            ),
        ),
        migrations.AddConstraint(
            model_name="equipment",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(
                        ("pole__isnull", False), ("segment__isnull", True)
                    ),
                    models.Q(
                        ("pole__isnull", True), ("segment__isnull", False)
                    ),
                    _connector="OR",
                ),
                name="cables_equipment_only_one_of_both_field_not_null_constraint",
            ),
        ),
    ]