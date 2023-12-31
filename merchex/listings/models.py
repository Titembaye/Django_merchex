from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Band(models.Model):
    def __str__(self):
        return f'{self.name}'

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    name = models.fields.CharField(max_length=100)
    bibliography = models.fields.CharField(max_length=50)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)


class Listing(models.Model):
    class Type(models.TextChoices):
        Records = 'Records'
        Clothing = 'Clothing'
        Posters = 'Posters'
        Micellaneous = 'Micellaneous'
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.FloatField(default=20)
    year = models.fields.IntegerField(null=True, blank=True)
    type = models.fields.CharField(choices=Type.choices, max_length=20)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
