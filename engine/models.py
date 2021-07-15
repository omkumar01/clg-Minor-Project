from djongo import models

from django.core.validators import URLValidator


class OnPageData(models.Model):

    h1count = models.IntegerField(default=0)
    h2count = models.IntegerField(default=0)
    h3count = models.IntegerField(default=0)
    h4count = models.IntegerField(default=0)
    h5count = models.IntegerField(default=0)
    page_title = models.CharField()
    charset = models.CharField()
    viewport = models.CharField()
    keywords = models.CharField()
    description = models.CharField()
    robots = models.CharField()
    og_type = models.CharField()
    og_title = models.CharField()
    og_description = models.CharField()
    og_url = models.CharField()
    og_image = models.CharField()
    twitter_card = models.CharField()
    twitter_title = models.CharField()
    twitter_description = models.CharField()
    twitter_image = models.CharField()
    schema_exist = models.CharField()
    lang_exist = models.CharField()
    content = models.CharField()
    imgcount = models.CharField()
    img_alt_found = models.CharField()
    img_alt_not_found = models.CharField()

    class Meta:
        abstract = True


class Url(models.Model):
    input_link = models.URLField(
        validators=[
            URLValidator,
        ]
    )
    onpagedata = models.EmbeddedField(
        model_container=OnPageData,
        default=None,
        null=True,
    )
