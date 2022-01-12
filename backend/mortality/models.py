#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _
from sinp_nomenclatures.models import Item as Nomenclature

from commons.models import BaseModel


class Case(BaseModel):
    """Case model extending BaseModel model with metadata fields

    Describe a mortality case.
    """

    species = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "species"},
        null=True,
        blank=True,
        related_name="species_name",
        verbose_name=_("Species"),
        help_text=_("Species"),
    )
    nb_death = models.IntegerField(_("Number found dead"), default=1)
    death_cause = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "death_cause"},
        null=True,
        blank=True,
        related_name="+",
        verbose_name=_("Cause of death"),
        help_text=_("Cause of death"),
    )
    data_source = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "death_data_source"},
        null=True,
        blank=True,
        related_name="death_data_source",
        verbose_name=_("Mortality data source"),
        help_text=_("Mortality data source"),
    )
