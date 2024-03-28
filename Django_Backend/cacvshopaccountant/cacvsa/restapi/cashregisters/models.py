from datetime import datetime
from typing import (
    Self,
    LiteralString
)

from django.db.models import (
    Model,
    CASCADE,
    AutoField,
    CharField,
    ForeignKey,
    DateTimeField,
    DecimalField
)

from restapi.abstracts.models import (
    NestedModel,
    MiniModel
)


class CashRegisterModel(NestedModel):

    id: AutoField = None
    number: CharField = None
    fk_user_employee: ForeignKey = None

    id = AutoField('ID', primary_key=True)
    number = CharField('Caja', max_length=256)
    fk_user_employee = ForeignKey('users.UserEmployeeModel', on_delete=CASCADE, verbose_name='Usuario')

    class Meta:

        db_table: str = None
        verbose_name: str = None
        verbose_name_plural: str = None

        db_table = 'APIS_CASH_REGISTER'
        verbose_name = 'CAJA REGISTRADORA'
        verbose_name_plural = 'CAJAS REGISTRADORAS'

    def __str__(self: Self) -> LiteralString:
        return self.number


class CashRegisterOpeningModel(Model):

    id: AutoField = None
    fk_cash_register: ForeignKey = None
    opening_date: DateTimeField = None
    opening_amount: DecimalField = None

    id = AutoField('ID', primary_key=True)
    fk_cash_register = ForeignKey('cashregisters.CashRegisterModel', on_delete=CASCADE, verbose_name='Caja')
    opening_date = DateTimeField('Fecha de Apertura')
    opening_amount = DecimalField('Monto de Apertura', max_digits=11, decimal_places=2)

    class Meta:

        db_table: str = None
        verbose_name: str = None
        verbose_name_plural: str = None

        db_table = 'APIS_CASH_REGISTER_OPENING'
        verbose_name = 'APERTURA DE CAJA REGISTRADORA'
        verbose_name_plural = 'APERTURAS DE CAJA REGISTRADORA'

    def __str__(self: Self) -> LiteralString:
        return self.fk_cash_register


class CashRegisterMovementsModel(MiniModel):

    id: AutoField = None
    fk_cash_register: ForeignKey = None
    movements_date: DateTimeField = None
    movements_detail: CharField = None
    fk_way_to_pay: ForeignKey = None
    movements_type: CharField = None
    movements_amount: DecimalField = None

    id = AutoField('ID', primary_key=True)
    fk_cash_register = ForeignKey('cashregisters.CashRegisterModel', on_delete=CASCADE, verbose_name='Caja')
    movements_date = DateTimeField('Fecha de Movimiento')
    movements_detail = CharField('Detalle', max_length=500)
    fk_way_to_pay = ForeignKey('business.WayToPayModel', on_delete=CASCADE, verbose_name='Forma de Pago')
    movements_type = CharField('Tipo', max_length=100)
    movements_amount = DecimalField('Monto', max_digits=11, decimal_places=2)

    class Meta:

        db_table: str = None
        verbose_name: str = None
        verbose_name_plural: str = None

        db_table = 'APIS_CASH_REGISTER_MOVEMENTS'
        verbose_name = 'MOVIMIENTO DE CAJA REGISTRADORA'
        verbose_name_plural = 'MOVIMIENTOS DE CAJA REGISTRADORA'

    def __str__(self: Self) -> LiteralString:
        return self.fk_cash_register


class CashRegisterClosingModel(Model):

    id: AutoField = None
    fk_cash_register: ForeignKey = None
    closing_date: DateTimeField = None
    total_sales: DecimalField = None
    total_transfers: DecimalField = None
    total_cash: DecimalField = None
    missing_or_surplus: DecimalField = None
    closing_amount: DecimalField = None
    remark: CharField = None

    id = AutoField('ID', primary_key=True)
    fk_cash_register = ForeignKey('cashregisters.CashRegisterModel', on_delete=CASCADE, verbose_name='Caja')
    closing_date = DateTimeField('Fecha de Cierre')
    total_sales = DecimalField('Total de Ventas', max_digits=11, decimal_places=2)
    total_transfers = DecimalField('Total Transferencias', max_digits=11, decimal_places=2)
    total_cash = DecimalField('Total en Efectivo', max_digits=11, decimal_places=2)
    missing_or_surplus = DecimalField('Faltante o Excedente', max_digits=11, decimal_places=2)
    closing_amount = DecimalField('Monto de Cierre', max_digits=11, decimal_places=2)
    remark = CharField('Observación', max_length=1024, default='Ninguna')

    class Meta:

        db_table: str = None
        verbose_name: str = None
        verbose_name_plural: str = None

        db_table = 'APIS_CASH_REGISTER_CLOSING'
        verbose_name = 'CIERRE DE CAJA REGISTRADORA'
        verbose_name_plural = 'CIERRES DE CAJA REGISTRADORA'

    def __str__(self: Self) -> LiteralString:
        return self.fk_cash_register
