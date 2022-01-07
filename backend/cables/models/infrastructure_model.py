# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-

# from uuid import uuid4

# from django.contrib.gis.db import models
from django.db import models
from django.utils.translation import gettext_lazy as _

from .base_model import BaseModel


class InfrastructureModel(BaseModel):
    """Common shared infrastructure model with metadata fields

    Abstract class: all specific infrastructure classes will inherit from this class
    """

    # uuid = models.UUIDField(
    #     default=uuid4,
    #     unique=True,
    #     editable=False,
    #     verbose_name=_("Identifiant unique"),
    # )
    # geocoord = models.PointField()
    remark = models.TextField(_("Remarque"), blank=True, null=True)

    class Meta:
        # app_label = 'cables'
        abstract = True


class PoleModel(InfrastructureModel):
    """Pole model extending infrastructure model with metadata fields

    Describe an electric pole.
    """

    class Meta:
        app_label = "cables"


class SegmentModel(InfrastructureModel):
    """Segment model extending infrastructure model with metadata fields

    Describe a power line segment.
    """

    class Meta:
        app_label = "cables"
