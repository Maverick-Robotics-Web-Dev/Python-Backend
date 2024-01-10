from django.db import models

class OwnCheckModel(models.Model):
    own_check_id = models.AutoField(primary_key=True)
    own_check_payment_date = models.DateField('Fecha de Pago')
    own_check_beneficiary = models.CharField('Beneficiario',max_length=500)
    own_check_detail = models.CharField('Detalle',max_length=500)
    own_check_voucher_type = models.CharField('Tipo de Comprobante', max_length=50)
    own_check_voucher_number = models.CharField('Numero de Comprobante',max_length=100, blank=True, null=True)
    own_check_deposit_date = models.DateField('Fecha de Deposito')
    own_check_bank = models.CharField('Banco',max_length=256)
    own_check_account_number = models.CharField('Numero de Cuenta',max_length=256)
    own_check_number = models.CharField('Cheque Numero',max_length=100)
    own_check_owner = models.CharField('Propietario',max_length=256)
    own_check_amount = models.DecimalField('Monto',max_digits=11, decimal_places=2)
    own_check_status = models.CharField('Estado', max_length=50)
    own_check_remark = models.CharField('Observaciones',max_length=500, blank=True, null=True)
    fk_user_employee = models.ForeignKey('users.UserEmployeeModel', on_delete=models.CASCADE)
    own_check_create_at = models.DateTimeField('Fecha de Creación')
    own_check_upgrade_at = models.DateTimeField('Fecha de Actualización',blank=True, null=True)

    class Meta:
        db_table = 'APIS_OWN_CHECK'
        verbose_name = 'CHEQUE PROPIO'
        verbose_name_plural = 'CHEQUES PROPIOS'
