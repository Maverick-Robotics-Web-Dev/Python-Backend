from django.db import models

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


class OwnCheck(models.Model):
    own_check_id = models.AutoField(primary_key=True)
    own_check_discharge_date = models.DateField()
    own_check_beneficiary = models.CharField(max_length=500)
    own_check_concept = models.CharField(max_length=500)
    own_check_voucher_number = models.CharField(max_length=100, blank=True, null=True)
    own_check_deposit_or_payment_date = models.DateField()
    own_check_bank = models.CharField(max_length=256)
    own_check_account_number = models.CharField(max_length=256)
    own_check_number = models.CharField(max_length=100)
    own_check_owner = models.CharField(max_length=256)
    own_check_amount = models.DecimalField(max_digits=11, decimal_places=2)
    own_check_status = models.CharField(max_length=256)
    own_check_remark = models.CharField(max_length=500, blank=True, null=True)
    user_employee = models.ForeignKey('UserEmployee', models.DO_NOTHING)
    own_check_create_at = models.DateTimeField()
    own_check_upgrade_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'OWN_CHECK'
        verbose_name = 'CHEQUE PROPIO'
        verbose_name_plural = 'CHEQUES PROPIOS'