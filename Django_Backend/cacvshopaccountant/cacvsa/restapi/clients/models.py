from typing import Self, LiteralString

from django.db.models import (
    CASCADE,
    AutoField,
    CharField,
    ForeignKey,
    DateField,
    DecimalField,
)

from restapi.abstracts.models import NestedModel


class ClientModel(NestedModel):

    id: AutoField = None
    code: CharField = None
    name: CharField = None
    trade_name: CharField = None
    branch_office_address_one: CharField = None
    branch_office_address_two: CharField = None
    branch_office_address_three: CharField = None
    branch_office_address_four: CharField = None
    phone_number_one: CharField = None
    phone_number_two: CharField = None
    phone_number_three: CharField = None
    phone_number_four: CharField = None
    fk_user_employee: ForeignKey = None

    id = AutoField('ID', primary_key=True)
    code = CharField('Codigo de Cliente', max_length=50)
    name = CharField('Appelidos y Nombre', max_length=500)
    trade_name = CharField('Nombre Comercial', max_length=500, blank=True, null=True)
    branch_office_address_one = CharField('Dirección', max_length=200, default='Sin Sucursal')
    branch_office_address_two = CharField('Dirección', max_length=200, default='Sin Sucursal')
    branch_office_address_three = CharField('Dirección', max_length=200, default='Sin Sucursal')
    branch_office_address_four = CharField('Dirección', max_length=200, default='Sin Sucursal')
    phone_number_one = CharField('Telefono', max_length=50, default='No posee numero telefonico')
    phone_number_two = CharField('Telefono', max_length=50, default='No posee numero telefonico')
    phone_number_three = CharField('Telefono', max_length=50, default='No posee numero telefonico')
    phone_number_four = CharField('Telefono', max_length=50, default='No posee numero telefonico')
    fk_user_employee = ForeignKey('users.UserEmployeeModel', on_delete=CASCADE, verbose_name='Usuario')

    class Meta:

        db_table: str = None
        verbose_name: str = None
        verbose_name_plural: str = None

        db_table = 'APIS_CLIENT'
        verbose_name = 'CLIENTE'
        verbose_name_plural = 'CLIENTES'

    def __str__(self: Self) -> LiteralString:
        return self.name


class ClientCheckModel(NestedModel):

    id: AutoField = None
    date_admission: DateField = None
    fk_client: ForeignKey = None
    detail: CharField = None
    voucher_type: CharField = None
    voucher_number: CharField = None
    deposit_date: DateField = None
    bank: CharField = None
    account_number: CharField = None
    check_number: CharField = None
    owner: CharField = None
    amount: DecimalField = None
    status: CharField = None
    deposited_in: CharField = None
    deposit_number: CharField = None
    endorsement_date: DateField = None
    discharge_date: DateField = None
    beneficiary: CharField = None
    remark: CharField = None
    fk_user_employee: ForeignKey = None

    id = AutoField('ID', primary_key=True)
    date_admission = DateField('Fecha de Admisión')
    fk_client = ForeignKey('clients.ClientModel', on_delete=CASCADE, verbose_name='Cliente')
    detail = CharField('Detalle', max_length=500)
    voucher_type = CharField('Tipo de Comprobante', max_length=256)
    voucher_number = CharField('Numero del Comprobante', max_length=100)
    deposit_date = DateField('Fecha de Deposito')
    bank = CharField('Banco', max_length=256)
    account_number = CharField('Numero de Cuenta', max_length=256)
    check_number = CharField('Numero de Cheque', max_length=100)
    owner = CharField('Propietario de la Cuenta', max_length=256)
    amount = DecimalField('Monto', max_digits=11, decimal_places=2)
    status = CharField('Estado', max_length=50)
    deposited_in = CharField('Depositado en Banco', max_length=256, blank=True, null=True)
    deposit_number = CharField('Numero de Comprobante', max_length=50, blank=True, null=True)
    endorsement_date = DateField('Fecha de Endoso', blank=True, null=True)
    discharge_date = DateField('Fecha de Descargo', blank=True, null=True)
    beneficiary = CharField('Beneficiario', max_length=500, blank=True, null=True)
    remark = CharField('Observaciones', max_length=500, default='Ninguna')
    fk_user_employee = ForeignKey('users.UserEmployeeModel', on_delete=CASCADE, verbose_name='Usuario')

    class Meta:

        db_table: str = None
        verbose_name: str = None
        verbose_name_plural: str = None

        db_table = 'APIS_CLIENT_CHECK'
        verbose_name = 'CHEQUE DEL CLIENTE'
        verbose_name_plural = 'CHEQUES DEL CLIENTE'

    def __str__(self: Self) -> LiteralString:
        return self.fk_client
