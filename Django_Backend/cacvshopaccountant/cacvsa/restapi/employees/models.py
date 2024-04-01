from typing import Self, LiteralString
from django.db.models import (
    CASCADE,
    AutoField,
    CharField,
    DateField,
    ForeignKey
)

from restapi.abstracts.models import (
    PersonModel,
    NestedModel
)


class EmployeeModel(PersonModel, NestedModel):

    id: AutoField = None
    code: CharField = None
    date_of_birth: DateField = None
    contract_type: CharField = None
    contract_code: CharField = None
    admission_date: DateField = None
    departure_date: DateField = None
    departament: CharField = None
    position: CharField = None
    extension_number: CharField = None
    fk_user_employee: ForeignKey = None

    id = AutoField('ID', primary_key=True)
    code = CharField('Codigo de Empleado', max_length=50)
    date_of_birth = DateField('Fecha de Nacimiento')
    contract_type = CharField('Tipo de Contrato', max_length=256, default='No posee contrato')
    contract_code = CharField('Codigo de Contrato', max_length=256, default='No posee codigo')
    admission_date = DateField('Fecha de Ingreso')
    departure_date = DateField('Fecha de Salida', blank=True, null=True)
    departament = CharField('Area o Departamento', max_length=256)
    position = CharField('Cargo', max_length=256)
    extension_number = CharField('Numero de Extensión', max_length=50, default='No Posee Extensión')
    fk_user_employee = ForeignKey('users.UserEmployeeModel', on_delete=CASCADE, verbose_name='Usuario')

    class Meta:

        db_table: str = None
        verbose_name: str = None
        verbose_name_plural: str = None

        db_table = 'APIS_EMPLOYEE'
        verbose_name = 'EMPLEADO'
        verbose_name_plural = 'EMPLEADOS'

    def __str__(self: Self) -> LiteralString:
        return self.name
