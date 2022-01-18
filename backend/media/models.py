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
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        related_name="media_author",
        verbose_name=_("Author of the media condition"),
        help_text=_("Author of the media condition"),
        on_delete=models.SET_NULL,
    )
    # visit = models.ForeignKey(
    #     Visit,
    #     null=True,
    #     blank=True,
    #     related_name="media_visit",
    #     verbose_name=_("Visit the media is related to"),
    #     help_text=_("Visit the media is related to"),
    #     on_delete=models.SET_NULL,
    # )
    # equipment = models.ForeignKey(
    #     Equipment,
    #     null=True,
    #     blank=True,
    #     related_name="media_equipment",
    #     verbose_name=_("Equipment the media is related to"),
    #     help_text=_("Equipment the media is related to"),
    #     on_delete=models.SET_NULL,
    # )
    # mortality = models.ForeignKey(
    #     Mortality,
    #     null=True,
    #     blank=True,
    #     related_name="media_mortality",
    #     verbose_name=_("Mortality observation the media is related to"),
    #     help_text=_("Mortality observation the media is related to"),
    #     on_delete=models.SET_NULL,
    # )

    class Meta:
        """Media_only_one_field_not_null_constraint

        Only one of three field is true:
        A media is associated with one Visit, or one Equipment or one Mortality observation
        """

    #     constraints = [
    #         models.CheckConstraint(
    #             name="Media_only_one_field_not_null_constraint",
    #             check=(
    #                 models.Q(visit=True, mortality=False)
    #                 | models.Q(visit=False, equipment=True, mortality=False)
    #                 | models.Q(visit=False, mortality=True)
    #             ),
    #         )
    #     ]


# class Media(BaseModel):
#     """Common shared Media model with metadata fields

#     Abstract class: all specific Media classes will inherit from this class.
#     This class describes media with related informations.
#     """

#     media = models.ImageField()
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         null=True,
#         blank=True,
#         related_name="media_author",
#         verbose_name=_("Author of the media condition"),
#         help_text=_("Author of the media condition"),
#         on_delete=models.SET_NULL,
#     )
