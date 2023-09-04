from django.db import models
from django.utils.translation import gettext_lazy as _

from commons.models import BaseModel


# Create your models here.
class News(BaseModel):
    title = models.CharField(_("Titre"), max_length=150)
    intro = models.CharField(_("Introduction"), max_length=500)
    body = models.TextField(_("Corps du texte"))
    private = models.BooleanField(_("Contenu privé"), default=True)

    class Meta:
        verbose_name_plural = _("News")


class Partners(BaseModel):
    name = models.CharField(_("Nom"), max_length=150)
    short_name = models.CharField(_("Nom court"), max_length=50)
    url = models.URLField(_("Site internet"), null=True, blank=True)
    logo = models.ImageField(
        _("Logo"),
        upload_to="partners/",
        height_field=None,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = _("Partners")
