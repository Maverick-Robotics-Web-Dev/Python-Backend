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

class Income(models.Model):
    income_id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING)
    income_voucher_type = models.CharField(max_length=256)
    income_establishment = models.CharField(max_length=50)
    income_billing_number = models.CharField(max_length=50)
    income_voucher_number = models.CharField(max_length=100)
    income_date = models.DateField()
    income_tax = models.DecimalField(max_digits=11, decimal_places=2)
    income_total = models.DecimalField(max_digits=11, decimal_places=2)
    user_employee = models.ForeignKey('UserEmployee', models.DO_NOTHING)
    income_status = models.IntegerField()
    income_status_description = models.CharField(max_length=256, blank=True, null=True)
    income_create_at = models.DateTimeField()

    class Meta:
        db_table = 'INCOME'
        verbose_name = 'INGRESO'
        verbose_name_plural = 'INGRESOS'

class IncomeDetail(models.Model):
    income_detail_id = models.AutoField(primary_key=True)
    income = models.ForeignKey('Income', models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    income_detail_quantity = models.DecimalField(max_digits=11, decimal_places=2)
    income_detail_purchase_price = models.DecimalField(max_digits=11, decimal_places=2)
    income_detail_sale_price = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        db_table = 'INCOME_DETAIL'
        verbose_name = 'DETALLE DE INGRESO'
        verbose_name_plural = 'DETALLES DE INGRESO'