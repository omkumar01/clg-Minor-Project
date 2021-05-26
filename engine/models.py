import django
from djongo import models

from django.core.validators import URLValidator


class Url(models.Model):
    input_link = models.URLField(validators=[URLValidator,])
    