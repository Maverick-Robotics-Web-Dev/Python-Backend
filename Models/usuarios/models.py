from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class UserLevel(models.Model):
    user_level_id = models.AutoField(primary_key=True)
    user_level_name = models.CharField('Nombre del Nivel',max_length=256)
    user_level_status = models.CharField('Estado', max_length=50)
    user_level_status_description = models.CharField('Descripción',max_length=256, blank=True, null=True)
    user_level_create_at = models.DateTimeField('Fecha de Creación')
    user_level_update_at = models.DateTimeField('Fecha de Actualización',blank=True, null=True)

    class Meta:
        db_table = 'USER_LEVEL'
        verbose_name = 'NIVEL DE USUARIO'
        verbose_name_plural = 'NIVELES DE USUARIO'

class UserEmployee(models.Model):
    user_employee_id = models.AutoField(primary_key=True)
    user_employee_user_name = models.CharField('Nombre de Usuario',max_length=256)
    user_employee_password = models.CharField('Contraseña',max_length=16)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    user_level = models.ForeignKey('UserLevel', on_delete=models.CASCADE)
    user_employee_login = models.BooleanField('Logueado')
    user_employee_status = models.CharField('Estado', max_length=50)
    user_employee_status_description = models.CharField('Descripción',max_length=256, default='Ninguna')
    user_employee_create_at = models.DateTimeField('Fecha de Creación')
    user_employee_update_at = models.DateTimeField('Fecha de Actualización',blank=True, null=True)

    # is_staff = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'USER_EMPLOYEE'
        verbose_name = 'USURIO DE EMPLEADO'
        verbose_name_plural = 'USUARIOS DE EMPLEADO'


class UserClient(models.Model):
    user_client_id = models.AutoField(primary_key=True)
    user_client_user_name = models.CharField('Nombre de Usuario',max_length=256)
    user_client_password = models.CharField('Contraseña',max_length=16)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    user_client_login = models.BooleanField('Logueado')
    user_client_status = models.CharField('Estado', max_length=50)
    user_client_status_description = models.CharField('Descripción',max_length=256, default='Ninguna')
    user_client_create_at = models.DateTimeField('Fecha de Creación')
    user_client_update_at = models.DateTimeField('Fecha de Actualización',blank=True, null=True)

    class Meta:
        db_table = 'USER_CLIENT'
        verbose_name = 'USUARIO DEL CLIENTE'
        verbose_name_plural = 'USUARIOS DEL CLIENTE'