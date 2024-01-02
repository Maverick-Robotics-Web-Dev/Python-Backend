from django.db import models

from abstract.models import *

class Employee(Person):
    employee_id = models.AutoField(primary_key=True)
    employee_code = models.CharField(max_length=50)
    employee_date_of_birth = models.DateField()
    employee_contract_type = models.CharField(max_length=256, blank=True, null=True)
    employee_contract_code = models.CharField(max_length=256, blank=True, null=True)
    employee_admission_date = models.DateField()
    employee_departure_date = models.DateField(blank=True, null=True)
    employee_departament = models.CharField(max_length=256)
    employee_position = models.CharField(max_length=256)
    employee_extension_number = models.CharField(max_length=50, blank=True, null=True)
    employee_status = models.IntegerField()
    employee_status_description = models.CharField(max_length=256, blank=True, null=True)
    user_employee = models.ForeignKey('UserEmployee', on_delete=models.CASCADE)
    employee_create_at = models.DateTimeField()
    employee_upgrade_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'EMPLOYEE'
        verbose_name = 'EMPLEADO'
        verbose_name_plural = 'EMPLEADOS'