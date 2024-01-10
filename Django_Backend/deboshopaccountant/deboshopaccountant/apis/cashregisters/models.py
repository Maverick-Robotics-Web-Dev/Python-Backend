from django.db import models

class CashRegisterModel(models.Model):
    cash_register_id = models.AutoField(primary_key=True)
    cash_register_number = models.CharField('Caja',max_length=256)
    fk_user_employee = models.ForeignKey('users.UserEmployeeModel', on_delete=models.CASCADE)
    cash_register_status = models.CharField('Estado', max_length=50)

    class Meta:
        db_table = 'APIS_CASH_REGISTER'
        verbose_name = 'CAJA REGISTRADORA'
        verbose_name_plural = 'CAJAS REGISTRADORAS'

class CashRegisterOpeningModel(models.Model):
    cash_register_opening_id = models.AutoField(primary_key=True)
    fk_cash_register = models.ForeignKey(CashRegisterModel, on_delete=models.CASCADE)
    cash_register_opening_date = models.DateTimeField('Fecha')
    cash_register_opening_amount = models.DecimalField('Monto de Apertura',max_digits=11, decimal_places=2)

    class Meta:
        db_table = 'APIS_CASH_REGISTER_OPENING'
        verbose_name = 'APERTURA DE CAJA REGISTRADORA'
        verbose_name_plural='APERTURAS DE CAJA REGISTRADORA'

class CashRegisterMovementsModel(models.Model):
    cash_register_movements_id = models.AutoField(primary_key=True)
    fk_cash_register = models.ForeignKey(CashRegisterModel, on_delete=models.CASCADE)
    cash_register_movements_date = models.DateTimeField('Fecha')
    cash_register_movements_detail = models.CharField('Detalle',max_length=500)
    fk_way_to_pay = models.ForeignKey('business.WayToPayModel', on_delete=models.CASCADE)
    cash_register_movements_type = models.CharField('Tipo',max_length=100)
    cash_register_movements_amount = models.DecimalField('Monto',max_digits=11, decimal_places=2)
    cash_register_movements_created_at = models.DateTimeField('Fecha de Creación')
    cash_register_movements_update_at = models.DateTimeField('Fecha de Actualización',blank=True, null=True)

    class Meta:
        db_table = 'APIS_CASH_REGISTER_MOVEMENTS'
        verbose_name = 'MOVIMIENTO DE CAJA REGISTRADORA'
        verbose_name_plural = 'MOVIMIENTOS DE CAJA REGISTRADORA'

class CashRegisterClosingModel(models.Model):
    cash_register_closing_id = models.AutoField(primary_key=True)
    fk_cash_register = models.ForeignKey(CashRegisterModel, on_delete=models.CASCADE)
    cash_register_closing_date = models.DateTimeField('Fecha')
    cash_register_closing_total_voucher_transactions = models.DecimalField('Total de Ventas',max_digits=11, decimal_places=2)
    cash_register_closing_total_cash_equivalent = models.DecimalField('Total Transferencias',max_digits=11, decimal_places=2)
    cash_register_closing_total_cash = models.DecimalField('Total en Efectivo',max_digits=11, decimal_places=2)
    cash_register_closing_missing_or_surplus = models.DecimalField('Faltante o Excedente',max_digits=11, decimal_places=2)
    cash_register_closing_amount = models.DecimalField('Monto de Cierre',max_digits=11, decimal_places=2)
    cash_register_closing_remark = models.CharField('Observación',max_length=1024, default='Ninguna')

    class Meta:
        db_table = 'APIS_CASH_REGISTER_CLOSING'
        verbose_name = 'CIERRE DE CAJA REGISTRADORA'
        verbose_name_plural = 'CIERRES DE CAJA REGISTRADORA'
