#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from django.contrib.gis.db import models as gis_models
from django.db import models
from django.utils.translation import gettext_lazy as _
from sinp_nomenclatures.models import Item as Nomenclature


class GeoArea(models.Model):
    """Class inheriting from sinp_nomenclature Item (refer sinp_nomenclature module).

    This class describes a nomenclature Item containing geometry attribute (PolygonField).
    As for nomenclature Items, instances of this class is related to a nomenclature Type, itself related to a nomenclature Source.
    """

    name = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "geoarea_name"},
        null=True,
        related_name="geoarea_name",
        verbose_name=_("Name of the geographical area"),
        help_text=_("Name of the geographical area"),
    )
    geom = gis_models.PolygonField(null=True, blank=True, srid=4326)

    class Meta:
        db_table = "geo_area"
