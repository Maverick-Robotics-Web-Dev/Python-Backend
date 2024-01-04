from django.db import models

from apis.abstracts.models import *

class ClientModel(PersonModel):
    client_id = models.AutoField(primary_key=True)
    client_code = models.CharField('Codigo de Cliente',max_length=50)
    client_trade_name = models.CharField('Nombre Comercial',max_length=500, blank=True, null=True)
    client_branch_office_address_one = models.CharField('Dirección',max_length=200, default='Sin Sucursal')
    client_branch_office_address_two = models.CharField('Dirección',max_length=200, default='Sin Sucursal')
    client_branch_office_address_three = models.CharField('Dirección',max_length=200, default='Sin Sucursal')
    client_branch_office_address_four = models.CharField('Dirección',max_length=200, default='Sin Sucursal')
    client_phone_number_one = models.CharField('Telefono',max_length=50, default='No posee numero telefonico')
    client_phone_number_two = models.CharField('Telefono',max_length=50, default='No posee numero telefonico')
    client_phone_number_three = models.CharField('Telefono',max_length=50, default='No posee numero telefonico')
    client_phone_number_four = models.CharField('Telefono',max_length=50, default='No posee numero telefonico')
    client_status = models.CharField('Estado', max_length=50)
    client_status_description = models.CharField('Descripción',max_length=256, blank=True, null=True)
    fk_user_employee = models.ForeignKey('users.UserEmployeeModel', on_delete=models.CASCADE)
    client_create_at = models.DateTimeField('Fecha de Creación')
    client_upgrade_at = models.DateTimeField('Fecha de Actulización',blank=True, null=True)

    class Meta:
        db_table = 'CLIENT'
        verbose_name = 'CLIENTE'
        verbose_name_plural = 'CLIENTES'

class ClientCheckModel(models.Model):
    client_check_id = models.AutoField(primary_key=True)
    client_check_date_admission = models.DateField('Fecha de Admisión')
    fk_client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    client_check_detail = models.CharField('Detalle',max_length=500)
    client_check_voucher_type = models.CharField('Tipo de Comprobante',max_length=256)
    client_check_voucher_number = models.CharField('Numero del Comprobante',max_length=100)
    client_check_deposit_date = models.DateField('Fecha de Deposito')
    client_check_bank = models.CharField('Banco',max_length=256)
    client_check_account_number = models.CharField('Numero de Cuenta',max_length=256)
    client_check_number = models.CharField('Numero de Cheque',max_length=100)
    client_check_owner = models.CharField('Propietario de la Cuenta',max_length=256)
    client_check_amount = models.DecimalField('Monto',max_digits=11, decimal_places=2)
    client_check_status = models.CharField('Estado', max_length=50)
    client_check_deposited_in = models.CharField('Depositado en Banco',max_length=256, blank=True, null=True)
    client_check_deposit_number = models.CharField('Numero de Comprobante', max_length=50, blank=True, null=True)
    client_check_endorsement_date = models.DateField('Fecha de Endoso',blank=True, null=True)
    client_check_discharge_date = models.DateField('Fecha de Descargo',blank=True, null=True)
    client_check_beneficiary = models.CharField('Beneficiario',max_length=500, blank=True, null=True)
    client_check_remark = models.CharField('Observaciones',max_length=500, default='Ninguna')
    fk_user_employee = models.ForeignKey('users.UserEmployeeModel', on_delete=models.CASCADE)
    client_check_create_at = models.DateTimeField('Fecha de Creación')
    client_check_upgrade_at = models.DateTimeField('Fecha de Actualizacion',blank=True, null=True)

    class Meta:
        db_table = 'CLIENT_CHECK'
        verbose_name = 'CHEQUE DEL CLIENTE'
        verbose_name_plural = 'CHEQUES DEL CLIENTE'
