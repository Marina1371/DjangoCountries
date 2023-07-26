from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=100)
    country_lang = models.CharField(max_length=100)


