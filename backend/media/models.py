#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from django.db import models
from django.utils.translation import gettext_lazy as _

from cables.models import PoleVisit, SegmentVisit
from commons.models import BaseModel


class Picture(BaseModel):
    """Common shared Picture model with metadata fields

    Abstract class: all specific Picture classes will inherit from this class.
    This class describes pictures with related informations.
    """

    # TODO to be completed with author at least
    picture = models.ImageField()

    class Meta:
        abstract = True


class PolePicture(BaseModel):
    """Common shared PolePicture model with metadata fields

    This class describes pole pictures with related informations.
    """

    # TODO to be completed with author at least
    picture = models.ImageField()
    polevisit = models.ForeignKey(
        PoleVisit,
        on_delete=models.CASCADE,
        related_name="polepicture_polevisit",
        verbose_name=_("Related pole visit"),
        help_text=_("Related pole visit"),
    )


class SegmentPicture(BaseModel):
    """Common shared SegmentPicture model with metadata fields

    This class describes segment pictures with related informations.
    """

    # TODO to be completed with author at least
    picture = models.ImageField()
    polesegment = models.ForeignKey(
        SegmentVisit,
        on_delete=models.CASCADE,
        related_name="polepicture_polesegment",
        verbose_name=_("Related pole segment"),
        help_text=_("Related pole segment"),
    )
