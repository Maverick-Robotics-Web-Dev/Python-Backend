from django.db import models

class Person(models.Model):
    document_type = models.CharField('Tipo de Documento',max_length=20)
    document_number = models.PositiveIntegerField('Numero',max_length=20)
    lastname = models.CharField('Apellidos',max_length=500)
    name = models.CharField('Nombres',max_length=500)
    country = models.CharField('Pais',max_length=200)
    state_province = models.CharField('Provincia o Estado',max_length=200)
    city = models.CharField('Ciudad',max_length=200)
    address = models.CharField('Dirección',max_length=200)
    postal_code = models.CharField('Codigo Postal', max_length=200, default='S/N')
    phone_number = models.CharField('Telefono',max_length=50, default='Sin Telefono Convencional')
    cellphone_number = models.CharField('Celular',max_length=50)
    email = models.CharField('E-mail',max_length=100, default='No Posee email')
    client_img = models.CharField('Imagen',max_length=500)

    class Meta:
        abstract = True
