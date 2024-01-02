from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class UserLevel(models.Model):
    user_level_id = models.AutoField(primary_key=True)
    user_level_name = models.CharField(max_length=256)
    user_level_status = models.IntegerField()
    user_level_status_description = models.CharField(max_length=256, blank=True, null=True)
    user_level_create_at = models.DateTimeField()
    user_level_update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'USER_LEVEL'
        verbose_name = 'NIVEL DE USUARIO'
        verbose_name_plural = 'NIVELES DE USUARIO'

class UserEmployee(models.Model):
    user_employee_id = models.AutoField(primary_key=True)
    user_employee_user_name = models.CharField(max_length=256)
    user_employee_password = models.CharField(max_length=16)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    user_level = models.ForeignKey('UserLevel', on_delete=models.CASCADE)
    user_employee_login = models.IntegerField()
    user_employee_status = models.IntegerField()
    user_employee_status_description = models.CharField(max_length=256, blank=True, null=True)
    user_employee_create_at = models.DateTimeField()
    user_employee_update_at = models.DateTimeField(blank=True, null=True)

    # is_staff = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'USER_EMPLOYEE'
        verbose_name = 'USURIO DE EMPLEADO'
        verbose_name_plural = 'USUARIOS DE EMPLEADO'


class UserClient(models.Model):
    user_client_id = models.AutoField(primary_key=True)
    user_client_user_name = models.CharField(max_length=256)
    user_client_password = models.CharField(max_length=16)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    user_client_login = models.IntegerField()
    user_client_status = models.IntegerField()
    user_client_status_description = models.CharField(max_length=256, blank=True, null=True)
    user_client_create_at = models.DateTimeField()
    user_client_update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'USER_CLIENT'
        verbose_name = 'USUARIO DEL CLIENTE'
        verbose_name_plural = 'USUARIOS DEL CLIENTE'