from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from restapi.users.managers import UserEmployeeManager


class UserLevelModel(models.Model):
    user_level_id = models.AutoField('ID', primary_key=True)
    user_level_name = models.CharField('Nombre del Nivel', max_length=256)
    user_level_status = models.CharField('Estado', max_length=50)
    user_level_status_description = models.CharField(
        'Descripción', max_length=256, blank=True, null=True)
    user_level_create_at = models.DateTimeField('Fecha de Creación')
    user_level_update_at = models.DateTimeField(
        'Fecha de Actualización', blank=True, null=True)

    class Meta:
        db_table = 'APIS_USER_LEVEL'
        verbose_name = 'NIVEL DE USUARIO'
        verbose_name_plural = 'NIVELES DE USUARIO'


class UserEmployeeModel(AbstractBaseUser, PermissionsMixin):

    user_employee_user_name = models.CharField(
        'Nombre de Usuario', max_length=20, unique=True)
    fk_employee = models.ForeignKey(
        'employees.EmployeeModel', on_delete=models.CASCADE, verbose_name='Empeado', blank=True, null=True)
    fk_user_level = models.ForeignKey(
        'users.UserLevelModel', on_delete=models.CASCADE, verbose_name='Nivel', blank=True, null=True)
    user_employee_login = models.BooleanField(
        'Logueado', blank=True, null=True, default=False)
    user_employee_status = models.BooleanField(
        'Estado', max_length=50, blank=True, null=True, default=False)
    user_employee_status_description = models.CharField(
        'Descripción', max_length=256, default='Ninguna')
    user_employee_create_at = models.DateTimeField(
        'Fecha de Creación', auto_now_add=True)
    user_employee_update_at = models.DateTimeField(
        'Fecha de Actualización', blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_employee_user_name'
    # REQUIRED_FIELDS=[]

    objects = UserEmployeeManager()

    class Meta:
        db_table = 'APIS_USER_EMPLOYEE'
        verbose_name = 'USURIO DE EMPLEADO'
        verbose_name_plural = 'USUARIOS DE EMPLEADO'


class UserClientModel(models.Model):
    user_client_id = models.AutoField('ID', primary_key=True)
    user_client_user_name = models.CharField(
        'Nombre de Usuario', max_length=256)
    user_client_password = models.CharField('Contraseña', max_length=16)
    fk_client = models.ForeignKey(
        'clients.ClientModel', on_delete=models.CASCADE, verbose_name='Cliente')
    user_client_login = models.BooleanField('Logueado')
    user_client_status = models.CharField('Estado', max_length=50)
    user_client_status_description = models.CharField(
        'Descripción', max_length=256, default='Ninguna')
    user_client_create_at = models.DateTimeField('Fecha de Creación')
    user_client_update_at = models.DateTimeField(
        'Fecha de Actualización', blank=True, null=True)

    class Meta:
        db_table = 'APIS_USER_CLIENT'
        verbose_name = 'USUARIO DEL CLIENTE'
        verbose_name_plural = 'USUARIOS DEL CLIENTE'
