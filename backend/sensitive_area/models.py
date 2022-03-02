#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from uuid import uuid4

from django.contrib.gis.db import models as gis_models
from django.db import models
from django.utils.translation import gettext_lazy as _

from commons.models import BaseModel

# from sinp_nomenclatures.models import  Nomenclature


class SensitiveArea(BaseModel):
    """SensibleArea model extending BaseModel model with metadata fields

    Describe a sensible area.

    uuid is a unique identifier (not primary key). It can be used as data identifier in case of
    data gathered from various origin (e.g. populating data from various DB)
    """

    uuid = models.UUIDField(
        default=uuid4,
        unique=True,
        editable=False,
        verbose_name=_("Identifiant unique"),
    )
    name = models.CharField(
        _("sensitive area name"), max_length=200
    )  # , null=True)
    code = models.CharField(max_length=100)  # , null=True)
    geom = gis_models.PolygonField(srid=4326)  # null=True, blank=True,

    def __str__(self):
        return f"{self.name} - [{self.code}]"

    class Meta:
        unique_together = [["code", "name"]]
        db_table = "sensitive_area"
