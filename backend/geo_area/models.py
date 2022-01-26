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

    name = models.CharField(_("geo area name"), max_length=200)
    code = models.CharField(max_length=100)

    type = models.ForeignKey(
        Nomenclature,
        on_delete=models.PROTECT,
        limit_choices_to={"type__mnemonic": "geoarea_type"},
        related_name="geoarea_type",
        verbose_name=_("Type of the geographical area"),
        help_text=_("Type of the geographical area"),
    )
    geom = gis_models.PolygonField(srid=4326)

    def __str__(self):
        return f"{self.name} - [{self.code}]"

    class Meta:
        unique_together = [["code", "name"]]
        db_table = "geo_area"
