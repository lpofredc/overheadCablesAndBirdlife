#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from sinp_nomenclatures.models import Item as Nomenclature

from commons.models import BaseModel


class Mortality(BaseModel):
    """Mortality model extending BaseModel model with metadata fields

    Describe a mortality case.
    """

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        related_name="mortality_author",
        verbose_name=_("Author of the mortality observation"),
        help_text=_("Author of the mortality observation"),
        on_delete=models.SET_NULL,
    )
    date_mortality = models.DateField(
        _("Mortality observation date"), default=timezone.now
    )
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
        limit_choices_to={"type__mnemonic": "cause_of_death"},
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
        related_name="mortality_data_source",
        verbose_name=_("Mortality data source"),
        help_text=_("Mortality data source"),
    )
    # PREV Fred relational suggestion with Media
    # media = models.ManyToManyField(
    #     Media,
    #     blank=True,
    #     related_name="mortality_media",
    #     verbose_name=_("Media related to the mortality case"),
    #     help_text=_("Media related to the mortality case"),
    # )

    def __str__(self):
        return f"Moratlity Case :{self.species} - {self.created_by} - {self.timestamp_create:%d-%m-%Y %H:%M}"
