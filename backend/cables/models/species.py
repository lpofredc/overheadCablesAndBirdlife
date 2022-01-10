from django.db import models


# TODO temporary species allowing creation of MortalityCase Model, awaiting this be defined
class Species(models.Model):
    class Meta:
        app_label = "cables"
