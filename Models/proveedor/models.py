from django.db import models

from abstract.models import *

class Supplier(Person):
    supplier_id = models.AutoField(primary_key=True)
    supplier_code = models.CharField(max_length=50)
    supplier_tradename = models.CharField(max_length=500, blank=True, null=True)
    supplier_branch_office_address_one = models.CharField(max_length=200, default='Sin Sucursal')
    supplier_branch_office_address_two = models.CharField(max_length=200, default='Sin Sucursal')
    supplier_branch_office_address_three = models.CharField(max_length=200, default='Sin Sucursal')
    supplier_branch_office_address_four = models.CharField(max_length=200, default='Sin Sucursal')
    supplier_phone_number_one = models.CharField(max_length=50, default='No posee numero telefonico')
    supplier_phone_number_two = models.CharField(max_length=50, default='No posee numero telefonico')
    supplier_phone_number_three = models.CharField(max_length=50, default='No posee numero telefonico')
    supplier_phone_number_four = models.CharField(max_length=50, default='No posee numero telefonico')
    user_employee = models.ForeignKey('UserEmployee', models.DO_NOTHING)
    supplier_status = models.IntegerField()
    supplier_status_description = models.CharField(max_length=256, blank=True, null=True)
    supplier_create_at = models.DateTimeField()
    supplier_upgrade_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'SUPPLIER'
        verbose_name = 'PROVEEDOR'
        verbose_name_plural = 'PROVEEDORES'