#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from django.contrib.gis.db import models as gis_models
from django.db import models
from django.utils.translation import gettext_lazy as _
from sinp_nomenclatures.models import Item as Nomenclature

"""These application models are using nomenclature Items 'cf. sinp_nomenclatures' module

    Item works like dictionnary term used to configure related application. Each Item is related to a Type, itself related to a Source. An application can authorize for a specific field to complete it with list of all Item terms with a defined Type (selected by Type mnemonic field). This allows to set up authorized entries for these field through database entries, not through hardcoded way,making application more flexible and more maintanable.
    """


class GeoArea(models.Model):
    """GeoArea model

    Define a geographical area that can be administrative area (city, department, region, ...) or natural area (Natura2000, ZNIEF, ...)
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
