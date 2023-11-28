from django.db import models

from .managers import *
# Create your models here.

class Author(models.Model):
    name = models.CharField("Nombre",max_length=50)
    surname = models.CharField("Apellido",max_length=50)
    nationality = models.CharField("Nacionalidad",max_length=30)
    age = models.PositiveIntegerField()
    objects = AuthorManager()

    def __str__(self):
        return f'{self.name}-{self.surname}'
