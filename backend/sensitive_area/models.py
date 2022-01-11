from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from sinp_nomenclatures.models import Item as Nomenclature

from trackable_basemodel.models import BaseModel


class SensitiveArea(BaseModel):
    """SensibleArea model extending BaseModel model with metadata fields

    Describe a sensible area.
    """

    sa_name_validator = UnicodeUsernameValidator()
    sa_name = models.CharField(
        _("sensible area name"),
        max_length=200,
        unique=True,
        help_text=_(
            "Required. 200 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[sa_name_validator],
        error_messages={
            "unique": _("A sensible area with that name already exists.")
        },
    )
    sensitivity_level = models.ForeignKey(
        Nomenclature,
        on_delete=models.DO_NOTHING,
        limit_choices_to={"type__mnemonic": "area_sensitivity_level"},
        related_name="+",
        verbose_name=_("Level of area sensitivity"),
        help_text=_("Sensitivity level of the area"),
    )

    class Meta:
        app_label = "sensitive_area"
