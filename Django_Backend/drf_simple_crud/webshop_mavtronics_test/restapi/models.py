# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CashRegister(models.Model):
    cash_register_id = models.AutoField(primary_key=True)
    cash_register_number = models.CharField(max_length=256)
    user_employee = models.ForeignKey('UserEmployee', models.DO_NOTHING)
    cash_register_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cash_register'


class CashRegisterClosing(models.Model):
    cash_register_closing_id = models.AutoField(primary_key=True)
    cash_register = models.ForeignKey(CashRegister, models.DO_NOTHING)
    cash_register_closing_date = models.DateTimeField()
    cash_register_closing_total_cash = models.DecimalField(
        max_digits=11, decimal_places=2)
    cash_register_closing_total_cash_equivalent = models.DecimalField(
        max_digits=11, decimal_places=2)
    cash_register_closing_total_voucher_transactions = models.DecimalField(
        max_digits=11, decimal_places=2)
    cash_register_closing_amount = models.DecimalField(
        max_digits=11, decimal_places=2)
    cash_register_closing_missing_or_surplus = models.DecimalField(
        max_digits=11, decimal_places=2)
    cash_register_closing_remark = models.CharField(
        max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_register_closing'


class CashRegisterMovements(models.Model):
    cash_register_movements_id = models.AutoField(primary_key=True)
    cash_register = models.ForeignKey(CashRegister, models.DO_NOTHING)
    cash_register_movements_date = models.DateTimeField()
    cash_register_movements_concept = models.CharField(max_length=500)
    way_to_pay = models.ForeignKey('WayToPay', models.DO_NOTHING)
    cash_register_movements_type = models.CharField(max_length=100)
    cash_register_movements_amount = models.DecimalField(
        max_digits=11, decimal_places=2)
    cash_register_movements_created_at = models.DateTimeField()
    cash_register_movements_update_at = models.DateTimeField(
        blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_register_movements'


class CashRegisterOpening(models.Model):
    cash_register_opening_id = models.AutoField(primary_key=True)
    cash_register = models.ForeignKey(CashRegister, models.DO_NOTHING)
    cash_register_opening_date = models.DateTimeField()
    cash_register_opening_amount = models.DecimalField(
        max_digits=11, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cash_register_opening'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_code = models.CharField(max_length=50)
    category_name = models.CharField(max_length=50)
    category_description = models.CharField(
        max_length=256, blank=True, null=True)
    category_img = models.CharField(max_length=256)
    category_status = models.IntegerField()
    category_status_description = models.CharField(
        max_length=256, blank=True, null=True)
    user_employee = models.ForeignKey('UserEmployee', models.DO_NOTHING)
    category_create_at = models.DateTimeField()
    category_update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_code = models.CharField(max_length=50)
    client_document_type = models.CharField(max_length=20)
    client_document_number = models.CharField(max_length=20)
    client_lastname = models.CharField(max_length=500)
    client_name = models.CharField(max_length=500)
    client_tradename = models.CharField(max_length=500, blank=True, null=True)
    client_country = models.CharField(max_length=200)
    client_state_province = models.CharField(max_length=200)
    client_city = models.CharField(max_length=200)
    client_home_address = models.CharField(max_length=200)
    client_work_address = models.CharField(
        max_length=200, blank=True, null=True)
    client_phone_number = models.CharField(
        max_length=50, blank=True, null=True)
    client_cellphone_number = models.CharField(max_length=50)
    client_workphone_number = models.CharField(
        max_length=50, blank=True, null=True)
    client_email = models.CharField(max_length=100, blank=True, null=True)
    client_img = models.CharField(max_length=256)
    client_status = models.IntegerField()
    client_status_description = models.CharField(
        max_length=256, blank=True, null=True)
    user_employee = models.ForeignKey('UserEmployee', models.DO_NOTHING)
    client_create_at = models.DateTimeField()
    client_upgrade_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'


class ClientCheck(models.Model):
    client_check_id = models.AutoField(primary_key=True)
    client_check_date_admission = models.DateField()
    client = models.ForeignKey(Client, models.DO_NOTHING)
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
    client_check_deposited_in = models.CharField(
        max_length=256, blank=True, null=True)
    client_check_endorsement_date = models.DateField(blank=True, null=True)
    client_check_discharge_date = models.DateField(blank=True, null=True)
    client_check_beneficiary = models.CharField(
        max_length=500, blank=True, null=True)
    client_check_remark = models.CharField(
        max_length=500, blank=True, null=True)
    user_employee = models.ForeignKey('UserEmployee', models.DO_NOTHING)
    client_check_create_at = models.DateTimeField()
    client_check_upgrade_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_check'
        db_table_comment = '\t\t'


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_code = models.CharField(max_length=50)
    employee_document_type = models.CharField(max_length=20)
    employee_document_number = models.CharField(max_length=20)
    employee_lastname = models.CharField(max_length=500)
    employee_name = models.CharField(max_length=500)
    employee_date_of_birth = models.DateField()
    employee_country = models.CharField(max_length=200)
    employee_state_province = models.CharField(max_length=200)
    employee_city = models.CharField(max_length=200)
    employee_address = models.CharField(max_length=200)
    employee_phone_number = models.CharField(
        max_length=50, blank=True, null=True)
    employee_cellphone_number = models.CharField(max_length=50)
    employee_email = models.CharField(max_length=100, blank=True, null=True)
    employee_img = models.CharField(max_length=256)
    employee_contract_type = models.CharField(
        max_length=256, blank=True, null=True)
    employee_contract_code = models.CharField(
        max_length=256, blank=True, null=True)
    employee_admission_date = models.DateField()
    employee_departure_date = models.DateField(blank=True, null=True)
    employee_departament = models.CharField(max_length=256)
    employee_position = models.CharField(max_length=256)
    employee_extension_number = models.CharField(
        max_length=50, blank=True, null=True)
    employee_status = models.IntegerField()
    employee_status_description = models.CharField(
        max_length=256, blank=True, null=True)
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
    income_status_description = models.CharField(
        max_length=256, blank=True, null=True)
    income_create_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'income'


class IncomeDetail(models.Model):
    income_detail_id = models.AutoField(primary_key=True)
    income = models.ForeignKey(Income, models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    income_detail_quantity = models.DecimalField(
        max_digits=11, decimal_places=2)
    income_detail_purchase_price = models.DecimalField(
        max_digits=11, decimal_places=2)
    income_detail_sale_price = models.DecimalField(
        max_digits=11, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'income_detail'


class OwnCheck(models.Model):
    own_check_id = models.AutoField(primary_key=True)
    own_check_discharge_date = models.DateField()
    own_check_beneficiary = models.CharField(max_length=500)
    own_check_concept = models.CharField(max_length=500)
    own_check_voucher_number = models.CharField(
        max_length=100, blank=True, null=True)
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


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_code = models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)
    product_barcode = models.CharField(max_length=50, blank=True, null=True)
    product_stock = models.IntegerField()
    product_presentation = models.CharField(max_length=256)
    product_price_in = models.DecimalField(max_digits=11, decimal_places=2)
    product_price_out = models.DecimalField(max_digits=11, decimal_places=2)
    product_img = models.CharField(max_length=256)
    product_description = models.CharField(
        max_length=256, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    user_employee = models.ForeignKey('UserEmployee', models.DO_NOTHING)
    product_status = models.IntegerField()
    product_status_description = models.CharField(
        max_length=256, blank=True, null=True)
    product_create_at = models.DateTimeField()
    product_update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


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
    sale_status_description = models.CharField(
        max_length=256, blank=True, null=True)
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
    supplier_document_type = models.CharField(max_length=20)
    supplier_document_number = models.CharField(max_length=20)
    supplier_lastname = models.CharField(max_length=500)
    supplier_name = models.CharField(max_length=500)
    supplier_tradename = models.CharField(
        max_length=500, blank=True, null=True)
    supplier_country = models.CharField(max_length=200)
    supplier_state_province = models.CharField(max_length=200)
    supplier_city = models.CharField(max_length=200)
    supplier_address = models.CharField(max_length=200, blank=True, null=True)
    supplier_phone_number = models.CharField(
        max_length=50, blank=True, null=True)
    supplier_cellphone_number = models.CharField(max_length=50)
    supplier_email = models.CharField(max_length=100, blank=True, null=True)
    supplier_img = models.CharField(max_length=256)
    user_employee = models.ForeignKey('UserEmployee', models.DO_NOTHING)
    supplier_status = models.IntegerField()
    supplier_status_description = models.CharField(
        max_length=256, blank=True, null=True)
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
    user_admin_status_description = models.CharField(
        max_length=256, blank=True, null=True)
    user_admin_create_at = models.DateTimeField()
    user_admin_update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_admin'


class UserClient(models.Model):
    user_client_id = models.AutoField(primary_key=True)
    user_client_name = models.CharField(max_length=256)
    user_client_lastname = models.CharField(max_length=256)
    user_client_user_name = models.CharField(max_length=256)
    user_client_password = models.CharField(max_length=16)
    user_client_login = models.IntegerField()
    user_client_status = models.IntegerField()
    user_client_status_description = models.CharField(
        max_length=256, blank=True, null=True)
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
    user_employee_status_description = models.CharField(
        max_length=256, blank=True, null=True)
    user_employee_create_at = models.DateTimeField()
    user_employee_update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_employee'


class UserLevel(models.Model):
    user_level_id = models.AutoField(primary_key=True)
    user_level_name = models.CharField(max_length=256)
    user_level_status = models.IntegerField()
    user_level_status_description = models.CharField(
        max_length=256, blank=True, null=True)
    user_level_create_at = models.DateTimeField()
    user_level_update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_level'


class WayToPay(models.Model):
    way_to_pay_id = models.AutoField(primary_key=True)
    way_to_pay_name = models.CharField(max_length=100)
    way_to_pay_description = models.CharField(
        max_length=256, blank=True, null=True)
    way_to_pay_create_at = models.DateTimeField()
    way_to_pay_update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'way_to_pay'
