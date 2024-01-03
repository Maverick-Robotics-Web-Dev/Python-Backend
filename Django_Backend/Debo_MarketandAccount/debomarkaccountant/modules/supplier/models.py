from django.db import models

from modules.abstracts.models import *

class Supplier(Person):
    supplier_id = models.AutoField(primary_key=True)
    supplier_code = models.CharField('Codigo de Proveedor',max_length=50)
    supplier_tradename = models.CharField('Nombre Comercial',max_length=500, blank=True, null=True)
    supplier_branch_office_address_one = models.CharField('Dirección',max_length=200, default='Sin Sucursal')
    supplier_branch_office_address_two = models.CharField('Dirección',max_length=200, default='Sin Sucursal')
    supplier_branch_office_address_three = models.CharField('Dirección',max_length=200, default='Sin Sucursal')
    supplier_branch_office_address_four = models.CharField('Dirección',max_length=200, default='Sin Sucursal')
    supplier_phone_number_one = models.CharField('Telefono',max_length=50, default='No posee numero telefonico')
    supplier_phone_number_two = models.CharField('Telefono',max_length=50, default='No posee numero telefonico')
    supplier_phone_number_three = models.CharField('Telefono',max_length=50, default='No posee numero telefonico')
    supplier_phone_number_four = models.CharField('Telefono',max_length=50, default='No posee numero telefonico')
    user_employee = models.ForeignKey('UserEmployee', on_delete=models.CASCADE)
    supplier_status = models.CharField('Estado', max_length=50)
    supplier_status_description = models.CharField('Descripción',max_length=256, default='Ninguna')
    supplier_create_at = models.DateTimeField('Fecha de Creación')
    supplier_upgrade_at = models.DateTimeField('Fecha de Actualizacion',blank=True, null=True)

    class Meta:
        db_table = 'SUPPLIER'
        verbose_name = 'PROVEEDOR'
        verbose_name_plural = 'PROVEEDORES'

class Income(models.Model):
    income_id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    income_voucher_type = models.CharField('Tipo de Comprobate',max_length=256)
    income_voucher_number = models.CharField('Numero de Comprobante',max_length=100)
    income_date = models.DateField('Fecha de Ingreso')
    income_tax_percentage = models.DecimalField('Porcentaje IVA', max_digits=11, decimal_places=2)
    income_tax = models.DecimalField('IVA',max_digits=11, decimal_places=2)
    income_total = models.DecimalField('Total',max_digits=11, decimal_places=2)
    user_employee = models.ForeignKey('UserEmployee', on_delete=models.CASCADE)
    income_status = models.CharField('Estado', max_length=50)
    income_status_description = models.CharField('Descripción', max_length=256, default='Ninguno')
    income_create_at = models.DateTimeField('Fecha de Creación')

    class Meta:
        db_table = 'INCOME'
        verbose_name = 'INGRESO'
        verbose_name_plural = 'INGRESOS'

class IncomeDetail(models.Model):
    income_detail_id = models.AutoField(primary_key=True)
    income = models.ForeignKey('Income', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    income_detail_quantity = models.DecimalField('Cantidad',max_digits=11, decimal_places=2)
    income_detail_purchase_price = models.DecimalField('Precio de Compra',max_digits=11, decimal_places=2)
    income_detail_sale_price = models.DecimalField('Precio de Venta',max_digits=11, decimal_places=2)

    class Meta:
        db_table = 'INCOME_DETAIL'
        verbose_name = 'DETALLE DE INGRESO'
        verbose_name_plural = 'DETALLES DE INGRESO'
