from typing import Self, LiteralString
from django.db.models import (
    CASCADE,
    AutoField,
    DateField,
    CharField,
    DecimalField,
    ForeignKey
)

from restapi.abstracts.models import MiniModel


class OwnCheckModel(MiniModel):

    id: AutoField = None
    payment_date: DateField = None
    beneficiary: CharField = None
    detail: CharField = None
    voucher_type: CharField = None
    voucher_number: CharField = None
    deposit_date: DateField = None
    bank: CharField = None
    account_number: CharField = None
    check_number: CharField = None
    check_owner: CharField = None
    amount: DecimalField = None
    status: CharField = None
    remark: CharField = None
    fk_user_employee: ForeignKey = None

    id = AutoField('ID', primary_key=True)
    payment_date = DateField('Fecha de Pago')
    beneficiary = CharField('Beneficiario', max_length=500)
    detail = CharField('Detalle', max_length=500)
    voucher_type = CharField('Tipo de Comprobante', max_length=50)
    voucher_number = CharField('Numero de Comprobante', max_length=100, blank=True, null=True)
    deposit_date = DateField('Fecha de Deposito')
    bank = CharField('Banco', max_length=256)
    account_number = CharField('Numero de Cuenta', max_length=256)
    check_number = CharField('Cheque Numero', max_length=100)
    check_owner = CharField('Propietario', max_length=256)
    amount = DecimalField('Monto', max_digits=11, decimal_places=2)
    status = CharField('Estado', max_length=50)
    remark = CharField('Observaciones', max_length=500, blank=True, null=True)
    fk_user_employee = ForeignKey('users.UserEmployeeModel', on_delete=CASCADE, verbose_name='Usuario')

    class Meta:

        db_table: str = None
        verbose_name: str = None
        verbose_name_plural: str = None

        db_table = 'APIS_OWN_CHECK'
        verbose_name = 'CHEQUE PROPIO'
        verbose_name_plural = 'CHEQUES PROPIOS'

    def __str__(self: Self) -> LiteralString:
        return self.payment_date
