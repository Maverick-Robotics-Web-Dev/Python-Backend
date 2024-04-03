from typing import Self, LiteralString

from django.db.models import (
    CASCADE,
    ForeignKey,
    AutoField,
    CharField,
    BooleanField
)
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from restapi.abstracts.models import NestedModel
from restapi.users.managers import UserEmployeeManager


class UserLevelModel(NestedModel):

    id: AutoField = None
    name: CharField = None
    fk_user_employee: ForeignKey = None

    id = AutoField('ID', primary_key=True)
    name = CharField('Nombre del Nivel', max_length=256)
    fk_user_employee = ForeignKey('users.UserEmployeeModel', on_delete=CASCADE, verbose_name='Usuario')

    class Meta:

        db_table: str = None
        verbose_name: str = None
        verbose_name_plural: str = None

        db_table = 'APIS_USER_LEVEL'
        verbose_name = 'NIVEL DE USUARIO'
        verbose_name_plural = 'NIVELES DE USUARIO'

    def __str__(self: Self) -> LiteralString:
        return self.name


class UserEmployeeModel(NestedModel, AbstractBaseUser, PermissionsMixin):

    id: AutoField = None
    user_name: CharField = None
    password: CharField = None
    fk_employee: ForeignKey = None
    fk_user_level: ForeignKey = None
    login: BooleanField = None
    is_superuser: BooleanField = None
    is_staff: BooleanField = None
    is_active: BooleanField = None
    USERNAME_FIELD: str = None
    objects: UserEmployeeManager = None

    id = AutoField('ID', primary_key=True)
    user_name = CharField('Nombre de Usuario', max_length=20, unique=True)
    password = CharField('Contraseña', max_length=16)
    fk_employee = ForeignKey('employees.EmployeeModel', on_delete=CASCADE, verbose_name='Empeado', blank=True, null=True)
    fk_user_level = ForeignKey('users.UserLevelModel', on_delete=CASCADE, verbose_name='Nivel', blank=True, null=True)
    login = BooleanField('Logueado', blank=True, null=True, default=False)
    is_superuser = BooleanField(default=False)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=False)

    USERNAME_FIELD = 'user_name'
    # REQUIRED_FIELDS=[]

    objects = UserEmployeeManager()

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'APIS_USER_EMPLOYEE'
        verbose_name = 'USURIO DE EMPLEADO'
        verbose_name_plural = 'USUARIOS DE EMPLEADO'


class UserClientModel(NestedModel):

    id: AutoField = None
    user_name: CharField = None
    password: CharField = None
    fk_client: ForeignKey = None
    login: BooleanField = None

    id = AutoField('ID', primary_key=True)
    user_name = CharField('Nombre de Usuario', max_length=256)
    password = CharField('Contraseña', max_length=16)
    fk_client = ForeignKey('clients.ClientModel', on_delete=CASCADE, verbose_name='Cliente')
    login = BooleanField('Logueado')

    class Meta:

        db_table: str = None
        verbose_name: str = None
        verbose_name_plural: str = None

        db_table = 'APIS_USER_CLIENT'
        verbose_name = 'USUARIO DEL CLIENTE'
        verbose_name_plural = 'USUARIOS DEL CLIENTE'

    def __str__(self: Self) -> LiteralString:
        return self.user_name
