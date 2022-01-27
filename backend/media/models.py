#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from commons.models import BaseModel


class Media(BaseModel):
    """Common shared Media model with metadata fields

    Abstract class: all specific Media classes will inherit from this class.
    This class describes media with related informations.
    """

    media = models.ImageField(upload_to="uploads/")
    author = models.CharField(_("Author"), max_length=200)
    date = models.DateField(_("Visit date"))
    source = models.CharField(_("Source of data"), max_length=200)
    remark = models.TextField(_("Remark"))
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        related_name="media_author",
        verbose_name=_("Author of the media condition"),
        help_text=_("Author of the media condition"),
        on_delete=models.SET_NULL,
    )
