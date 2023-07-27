from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=100)


class Country(models.Model):
    country_name = models.CharField(max_length=100)
    langs = models.ManyToManyField(Language)


