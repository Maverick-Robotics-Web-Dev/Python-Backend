from django.db import models

class CashRegister(models.Model):
    cash_register_id = models.AutoField(primary_key=True)
    cash_register_number = models.CharField(max_length=256)
    user_employee = models.ForeignKey('UserEmployee', on_delete=models.CASCADE)
    cash_register_status = models.IntegerField()

    class Meta:
        db_table = 'CASH_REGISTER'
        verbose_name = 'CAJA REGISTRADORA'
        verbose_name_plural = 'CAJAS REGISTRADORAS'

class CashRegisterOpening(models.Model):
    cash_register_opening_id = models.AutoField(primary_key=True)
    cash_register = models.ForeignKey('CashRegister', on_delete=models.CASCADE)
    cash_register_opening_date = models.DateTimeField()
    cash_register_opening_amount = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        db_table = 'CASH_REGISTER_OPENING'
        verbose_name = 'APERTURA DE CAJA REGISTRADORA'
        verbose_name_plural='APERTURAS DE CAJA REGISTRADORA'

class CashRegisterMovements(models.Model):
    cash_register_movements_id = models.AutoField(primary_key=True)
    cash_register = models.ForeignKey('CashRegister', on_delete=models.CASCADE)
    cash_register_movements_date = models.DateTimeField()
    cash_register_movements_concept = models.CharField(max_length=500)
    way_to_pay = models.ForeignKey('WayToPay', on_delete=models.CASCADE)
    cash_register_movements_type = models.CharField(max_length=100)
    cash_register_movements_amount = models.DecimalField(max_digits=11, decimal_places=2)
    cash_register_movements_created_at = models.DateTimeField()
    cash_register_movements_update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'CASH_REGISTER_MOVEMENTS'
        verbose_name = 'MOVIMIENTO DE CAJA REGISTRADORA'
        verbose_name_plural = 'MOVIMIENTOS DE CAJA REGISTRADORA'

class CashRegisterClosing(models.Model):
    cash_register_closing_id = models.AutoField(primary_key=True)
    cash_register = models.ForeignKey('CashRegister', on_delete=models.CASCADE)
    cash_register_closing_date = models.DateTimeField()
    cash_register_closing_total_cash = models.DecimalField(max_digits=11, decimal_places=2)
    cash_register_closing_total_cash_equivalent = models.DecimalField(max_digits=11, decimal_places=2)
    cash_register_closing_total_voucher_transactions = models.DecimalField(max_digits=11, decimal_places=2)
    cash_register_closing_amount = models.DecimalField(max_digits=11, decimal_places=2)
    cash_register_closing_missing_or_surplus = models.DecimalField(max_digits=11, decimal_places=2)
    cash_register_closing_remark = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        db_table = 'CASH_REGISTER_CLOSING'
        verbose_name = 'CIERRE DE CAJA REGISTRADORA'
        verbose_name_plural = 'CIERRES DE CAJA REGISTRADORA'