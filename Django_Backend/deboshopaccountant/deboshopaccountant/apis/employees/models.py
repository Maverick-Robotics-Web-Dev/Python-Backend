from django.db import models

from apis.abstracts.models import *

class EmployeeModel(PersonModel):
    employee_id = models.AutoField(primary_key=True)
    employee_code = models.CharField('Codigo de Empleado',max_length=50)
    employee_date_of_birth = models.DateField('Fecha de Nacimiento')
    employee_contract_type = models.CharField('Tipo de Contrato',max_length=256, default='No posee contrato')
    employee_contract_code = models.CharField('Codigo de Contrato',max_length=256, default='No posee codigo')
    employee_admission_date = models.DateField('Fecha de Ingreso')
    employee_departure_date = models.DateField('Fecha de Salida',blank=True, null=True)
    employee_departament = models.CharField('Area o Departamento',max_length=256)
    employee_position = models.CharField('Cargo',max_length=256)
    employee_extension_number = models.CharField('Numero de Extensión',max_length=50, default='No Posee Extensión')
    employee_status = models.CharField('Estado', max_length=50)
    employee_status_description = models.CharField('Descripción',max_length=256, default='Ninguna')
    fk_user_employee = models.ForeignKey('users.UserEmployeeModel', on_delete=models.CASCADE)
    employee_create_at = models.DateTimeField('Fecha de Creación')
    employee_upgrade_at = models.DateTimeField('Fecha Actualización',blank=True, null=True)

    class Meta:
        db_table = 'EMPLOYEE'
        verbose_name = 'EMPLEADO'
        verbose_name_plural = 'EMPLEADOS'