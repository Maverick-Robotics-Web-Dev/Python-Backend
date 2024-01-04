from django.db import models

from apis.abstracts.models import *
from apis.product.models import *
from apis.usersn.models import *

class SupplierModel(PersonModel):
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
    fk_user_employee = models.ForeignKey(UserEmployeeModel, on_delete=models.CASCADE)
    supplier_status = models.CharField('Estado', max_length=50)
    supplier_status_description = models.CharField('Descripción',max_length=256, default='Ninguna')
    supplier_create_at = models.DateTimeField('Fecha de Creación')
    supplier_upgrade_at = models.DateTimeField('Fecha de Actualizacion',blank=True, null=True)

    class Meta:
        db_table = 'SUPPLIER'
        verbose_name = 'PROVEEDOR'
        verbose_name_plural = 'PROVEEDORES'

class IncomeModel(models.Model):
    income_id = models.AutoField(primary_key=True)
    fk_supplier = models.ForeignKey(SupplierModel, on_delete=models.CASCADE)
    income_voucher_type = models.CharField('Tipo de Comprobate',max_length=256)
    income_voucher_number = models.CharField('Numero de Comprobante',max_length=100)
    income_date = models.DateField('Fecha de Ingreso')
    income_tax_percentage = models.DecimalField('Porcentaje IVA', max_digits=11, decimal_places=2)
    income_tax = models.DecimalField('IVA',max_digits=11, decimal_places=2)
    income_total = models.DecimalField('Total',max_digits=11, decimal_places=2)
    fk_user_employee = models.ForeignKey(UserEmployeeModel, on_delete=models.CASCADE)
    income_status = models.CharField('Estado', max_length=50)
    income_status_description = models.CharField('Descripción', max_length=256, default='Ninguno')
    income_create_at = models.DateTimeField('Fecha de Creación')

    class Meta:
        db_table = 'INCOME'
        verbose_name = 'INGRESO'
        verbose_name_plural = 'INGRESOS'

class IncomeDetailModel(models.Model):
    income_detail_id = models.AutoField(primary_key=True)
    fk_income = models.ForeignKey(IncomeModel, on_delete=models.CASCADE)
    fk_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    income_detail_quantity = models.DecimalField('Cantidad',max_digits=11, decimal_places=2)
    income_detail_purchase_price = models.DecimalField('Precio de Compra',max_digits=11, decimal_places=2)
    income_detail_sale_price = models.DecimalField('Precio de Venta',max_digits=11, decimal_places=2)

    class Meta:
        db_table = 'INCOME_DETAIL'
        verbose_name = 'DETALLE DE INGRESO'
        verbose_name_plural = 'DETALLES DE INGRESO'
