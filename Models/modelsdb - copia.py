# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

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



