from django.db import models

from abstract.models import *

class Client(Person):
    client_id = models.AutoField(primary_key=True)
    client_code = models.CharField(max_length=50)
    client_tradename = models.CharField(max_length=500, blank=True, null=True)
    client_branch_office_address_one = models.CharField(max_length=200, default='Sin Sucursal')
    client_branch_office_address_two = models.CharField(max_length=200, default='Sin Sucursal')
    client_branch_office_address_three = models.CharField(max_length=200, default='Sin Sucursal')
    client_branch_office_address_four = models.CharField(max_length=200, default='Sin Sucursal')
    client_phone_number_one = models.CharField(max_length=50, default='No posee numero telefonico')
    client_phone_number_two = models.CharField(max_length=50, default='No posee numero telefonico')
    client_phone_number_three = models.CharField(max_length=50, default='No posee numero telefonico')
    client_phone_number_four = models.CharField(max_length=50, default='No posee numero telefonico')
    client_status = models.IntegerField()
    client_status_description = models.CharField(max_length=256, blank=True, null=True)
    user_employee = models.ForeignKey('UserEmployee', models.DO_NOTHING)
    client_create_at = models.DateTimeField()
    client_upgrade_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'CLIENT'
        verbose_name = 'CLIENTE'
        verbose_name_plural = 'CLIENTES'

class ClientCheck(models.Model):
    client_check_id = models.AutoField(primary_key=True)
    client_check_date_admission = models.DateField()
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    client_check_concept = models.CharField(max_length=500)
    client_check_voucher_type = models.CharField(max_length=256)
    client_check_voucher_number = models.CharField(max_length=100)
    client_check_deposit_date = models.DateField()
    client_check_bank = models.CharField(max_length=256)
    client_check_account_number = models.CharField(max_length=256)
    client_check_number = models.CharField(max_length=100)
    client_check_owner = models.CharField(max_length=256)
    client_check_amount = models.DecimalField(max_digits=11, decimal_places=2)
    client_check_status = models.CharField(max_length=256)
    client_check_deposited_in = models.CharField(max_length=256, blank=True, null=True)
    client_check_endorsement_date = models.DateField(blank=True, null=True)
    client_check_discharge_date = models.DateField(blank=True, null=True)
    client_check_beneficiary = models.CharField(max_length=500, blank=True, null=True)
    client_check_remark = models.CharField(max_length=500, blank=True, null=True)
    user_employee = models.ForeignKey('UserEmployee', on_delete=models.CASCADE)
    client_check_create_at = models.DateTimeField()
    client_check_upgrade_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'CLIENT_CHECK'
        verbose_name = 'CHEQUE DEL CLIENTE'
        verbose_name_plural = 'CHEQUES DEL CLIENTE'