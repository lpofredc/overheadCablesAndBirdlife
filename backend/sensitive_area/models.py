#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from uuid import uuid4

from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.gis.db import models as gis_models
from django.db import models
from django.utils.translation import gettext_lazy as _

from commons.models import BaseModel


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
    geom = gis_models.PolygonField(null=True, blank=True, srid=4326)
    name_validator = UnicodeUsernameValidator()
    name = models.CharField(
        _("sensible area name"),
        max_length=200,
        unique=True,
        help_text=_(
            "Required. 200 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[name_validator],
        error_messages={
            "unique": _("A sensible area with that name already exists.")
        },
    )

    def __str__(self):
        return f"Sensitive Area :{self.name}"

    class Meta:
        db_table = "sensitive_area"
