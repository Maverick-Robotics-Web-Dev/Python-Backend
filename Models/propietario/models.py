from django.db import models

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