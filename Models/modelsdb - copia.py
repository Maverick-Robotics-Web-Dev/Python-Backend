# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class CreditNote(models.Model):
    credit_note_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    credit_note_voucher_number = models.CharField(max_length=100)
    credit_note_date = models.DateField()
    credit_note_total = models.DecimalField(max_digits=11, decimal_places=0)
    user_employee = models.ForeignKey('UserEmployee', models.DO_NOTHING)
    credit_note_status = models.IntegerField()
    credit_note_description = models.CharField(max_length=256, blank=True, null=True)
    credit_note_create_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'credit_note'


class CreditNoteDetail(models.Model):
    credit_note_detail_id = models.AutoField(primary_key=True)
    credit_note = models.ForeignKey(CreditNote, models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    credit_note_detail_quantity = models.DecimalField(max_digits=11, decimal_places=2)
    credit_note_detail_price = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'credit_note_detail'


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_code = models.CharField(max_length=50)
    employee_date_of_birth = models.DateField()
    employee_contract_type = models.CharField(max_length=256, blank=True, null=True)
    employee_contract_code = models.CharField(max_length=256, blank=True, null=True)
    employee_admission_date = models.DateField()
    employee_departure_date = models.DateField(blank=True, null=True)
    employee_departament = models.CharField(max_length=256)
    employee_position = models.CharField(max_length=256)
    employee_extension_number = models.CharField(max_length=50, blank=True, null=True)
    employee_status = models.IntegerField()
    employee_status_description = models.CharField(max_length=256, blank=True, null=True)
    user_employee = models.ForeignKey('UserEmployee', models.DO_NOTHING)
    employee_create_at = models.DateTimeField()
    employee_upgrade_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


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
        managed = False
        db_table = 'income'


class IncomeDetail(models.Model):
    income_detail_id = models.AutoField(primary_key=True)
    income = models.ForeignKey(Income, models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    income_detail_quantity = models.DecimalField(max_digits=11, decimal_places=2)
    income_detail_purchase_price = models.DecimalField(max_digits=11, decimal_places=2)
    income_detail_sale_price = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'income_detail'


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
        managed = False
        db_table = 'own_check'

class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    sale_voucher_type = models.CharField(max_length=256)
    sale_establishment = models.CharField(max_length=50)
    sale_billing_number = models.CharField(max_length=50)
    sale_voucher_number = models.CharField(max_length=100)
    sale_date = models.DateField()
    sale_tax = models.DecimalField(max_digits=11, decimal_places=2)
    sale_total = models.DecimalField(max_digits=11, decimal_places=2)
    way_to_pay = models.ForeignKey('WayToPay', models.DO_NOTHING)
    user_employee = models.ForeignKey('UserEmployee', models.DO_NOTHING)
    sale_status = models.IntegerField()
    sale_status_description = models.CharField(max_length=256, blank=True, null=True)
    sale_create_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sale'


class SaleDetail(models.Model):
    sale_detail_id = models.AutoField(primary_key=True)
    sale = models.ForeignKey(Sale, models.DO_NOTHING)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    sale_detail_quantity = models.DecimalField(max_digits=11, decimal_places=2)
    sale_detail_price = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'sale_detail'


class Supplier(models.Model):
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
        managed = False
        db_table = 'supplier'


class UserAdmin(models.Model):
    user_admin_id = models.AutoField(primary_key=True)
    user_admin_name = models.CharField(max_length=256)
    user_admin_lastname = models.CharField(max_length=256)
    user_admin_user_name = models.CharField(max_length=256)
    user_admin_password = models.CharField(max_length=16)
    user_admin_login = models.IntegerField()
    user_admin_status = models.IntegerField()
    user_admin_status_description = models.CharField(max_length=256, blank=True, null=True)
    user_admin_create_at = models.DateTimeField()
    user_admin_update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_admin'


class UserClient(models.Model):
    user_client_id = models.AutoField(primary_key=True)
    user_client_user_name = models.CharField(max_length=256)
    user_client_password = models.CharField(max_length=16)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    user_client_login = models.IntegerField()
    user_client_status = models.IntegerField()
    user_client_status_description = models.CharField(max_length=256, blank=True, null=True)
    user_client_create_at = models.DateTimeField()
    user_client_update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_client'


class UserEmployee(models.Model):
    user_employee_id = models.AutoField(primary_key=True)
    user_employee_name = models.CharField(max_length=256)
    user_employee_lastname = models.CharField(max_length=256)
    user_employee_user_name = models.CharField(max_length=256)
    user_employee_password = models.CharField(max_length=16)
    user_level = models.ForeignKey('UserLevel', models.DO_NOTHING)
    user_employee_login = models.IntegerField()
    user_employee_status = models.IntegerField()
    user_employee_status_description = models.CharField(max_length=256, blank=True, null=True)
    user_employee_create_at = models.DateTimeField()
    user_employee_update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_employee'


class UserLevel(models.Model):
    user_level_id = models.AutoField(primary_key=True)
    user_level_name = models.CharField(max_length=256)
    user_level_status = models.IntegerField()
    user_level_status_description = models.CharField(max_length=256, blank=True, null=True)
    user_level_create_at = models.DateTimeField()
    user_level_update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_level'


class WayToPay(models.Model):
    way_to_pay_id = models.AutoField(primary_key=True)
    way_to_pay_name = models.CharField(max_length=100)
    way_to_pay_description = models.CharField(max_length=256, blank=True, null=True)
    way_to_pay_create_at = models.DateTimeField()
    way_to_pay_update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'way_to_pay'
