from django.db import models
from modules.libro.models import Book

# Create your models here.

class Reader(models.Model):
    names = models.CharField("Nombres", max_length=50)
    surnames = models.CharField("Apellidos", max_length=50)
    nationality = models.CharField("Nacionalidad", max_length=20)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.names
    
class Loan(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateField()
    come_back_date = models.DateField(blank=True, null=True)
    status = models.BooleanField()

    def __str__(self):
        return self.book.title