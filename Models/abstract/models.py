from django.db import models

class Person(models.Model):
    document_type = models.CharField(max_length=20)
    document_number = models.PositiveIntegerField(max_length=20)
    lastname = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    country = models.CharField(max_length=200)
    state_province = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50, default='Sin Telefono Convencional')
    cellphone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=100, default='No Posee email')
    client_img = models.CharField(max_length=256)

    class Meta:
        abstract = True
