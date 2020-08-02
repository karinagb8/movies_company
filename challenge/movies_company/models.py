from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Alias(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = 'Aliases'

    def __str__(self):
        return self.name


class Person(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    aliases = models.ManyToManyField('Alias')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Movie(models.Model):
    title = models.CharField(max_length=300)
    release_year = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(3999),
            MinValueValidator(1)
        ]
    )
    casting = models.ManyToManyField(
        'Person',
        related_name='movies_as_actor_actress'
    )
    directors = models.ManyToManyField(
        'Person',
        related_name='movies_as_director'
    )
    producers = models.ManyToManyField(
        'Person',
        related_name='movies_as_producer'
    )

    def __str__(self):
        return self.title + ' (' + str(self.release_year) + ')'
