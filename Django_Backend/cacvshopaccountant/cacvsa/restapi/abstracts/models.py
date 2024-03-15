from django.db.models import *


class PersonModel(Model):

    document_type: CharField = None
    document_number: PositiveIntegerField = None
    lastname: CharField = None
    name: CharField = None
    country: CharField = None
    state_province: CharField = None
    city: CharField = None
    address: CharField = None
    postal_code: CharField = None
    phone_number: CharField = None
    cellphone_number: CharField = None
    email: CharField = None
    img: ImageField = None

    document_type = CharField('Tipo de Documento', max_length=20)
    document_number = PositiveIntegerField('Numero')
    lastname = CharField('Apellidos', max_length=500)
    name = CharField('Nombres', max_length=500)
    country = CharField('Pais', max_length=200)
    state_province = CharField('Provincia o Estado', max_length=200)
    city = CharField('Ciudad', max_length=200)
    address = CharField('Dirección', max_length=200)
    postal_code = CharField('Codigo Postal', max_length=200, default='S/N')
    phone_number = CharField('Telefono', max_length=50,
                             default='Sin Telefono Convencional')
    cellphone_number = CharField('Celular', max_length=50)
    email = CharField('E-mail', max_length=100, default='No Posee email')
    img = ImageField('Imagen', upload_to='persons/', blank=True, null=True)

    class Meta:
        abstract = True


class NestedModel(Model):

    status: BooleanField = None
    status_description: CharField = None
    create_at: DateTimeField = None
    update_at: DateTimeField = None

    status = BooleanField('Estado', default=False)
    status_description = CharField(
        'Descripción del Estado', max_length=256, default='No existe descripción')
    create_at = DateTimeField('Fecha de Creación')
    update_at = DateTimeField('Fecha de Actualización', blank=True, null=True)

    class Meta:
        abstract = True
