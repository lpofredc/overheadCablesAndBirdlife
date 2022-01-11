from django.conf import settings
from django.db import models


class BaseModel(
    models.Model
):  # base class should subclass 'django.db.models.Model'
    """Common shared base model with metadata fields

    Abstract class: all objects from classes extending this class will have references and timestamp of who create it and who updated it last tiem.
    """

    timestamp_create = models.DateTimeField(auto_now_add=True, editable=False)
    timestamp_update = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        db_index=True,
        editable=False,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        db_index=True,
        editable=False,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    class Meta:
        app_label = "trackable_basemodel"
        abstract = True
