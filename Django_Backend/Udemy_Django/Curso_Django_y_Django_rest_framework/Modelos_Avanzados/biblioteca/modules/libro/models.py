from django.db import models
from modules.autor.models import *

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
    title = models.CharField("Titutlo", max_length=50)
    release_date = models.DateField("Fecha de Lanzamiento")
    front_page = models.ImageField("Portada", upload_to='portada')
    visits = models.PositiveIntegerField()

    def __str__(self):
        return self.title
