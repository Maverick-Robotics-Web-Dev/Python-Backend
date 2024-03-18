from typing import LiteralString
from django.db.models import (
    CASCADE,
    AutoField,
    CharField,
    ForeignKey,
    DateField,
    DecimalField
)

from restapi.abstracts.models import NestedModel


class WayToPayModel(NestedModel):

    id: AutoField = None
    name: CharField = None
    description: CharField = None
    fk_user_employee: ForeignKey = None

    id = AutoField('ID', primary_key=True)
    name = CharField('Forma de Pago', max_length=100)
    description = CharField(
        'Descripcion', max_length=256, blank=True, null=True)
    fk_user_employee = ForeignKey(
        'users.UserEmployeeModel', on_delete=CASCADE, verbose_name='Usuario')

    class Meta:

        db_table: str = None
        verbose_name: str = None
        verbose_name_plural: str = None

        db_table = 'APIS_WAY_TO_PAY'
        verbose_name = 'FORMA DE PAGO'
        verbose_name_plural = 'FORMAS DE PAGO'

    def __str__(self) -> LiteralString:
        return self.name


class VoucherTypeModel(NestedModel):

    id: AutoField = None
    name: CharField = None
    description: CharField = None
    fk_user_employee: ForeignKey = None

    id = AutoField('ID', primary_key=True)
    name = CharField('Tipo de Comprobante', max_length=100)
    description = CharField(
        'Descripción', max_length=256, default='No existe descripción')
    fk_user_employee = ForeignKey(
        'users.UserEmployeeModel', on_delete=CASCADE, verbose_name='Usuario')

    class Meta:
        db_table = 'APIS_VOUCHER_TYPE'
        verbose_name = 'TIPO DE COMPROBANTE'
        verbose_name_plural = 'TIPOS DE COMPROBANTE'

    def __str__(self):
        return self.name


class CreditNoteModel(NestedModel):

    id: AutoField = None
    fk_client: ForeignKey = None
    voucher_number: CharField = None
    date: DateField = None
    total: DecimalField = None
    fk_user_employee: ForeignKey = None

    id = AutoField('ID', primary_key=True)
    fk_client = ForeignKey(
        'clients.ClientModel', on_delete=CASCADE, verbose_name='Cliente')
    voucher_number = CharField(
        'Numero de Comprobante', max_length=100)
    date = DateField('Fecha')
    total = DecimalField(
        'Total', max_digits=11, decimal_places=0)
    fk_user_employee = ForeignKey(
        'users.UserEmployeeModel', on_delete=CASCADE, verbose_name='Usuario')

    class Meta:
        db_table = 'APIS_CREDIT_NOTE'
        verbose_name = 'NOTA DE CREDITO'
        verbose_name_plural = 'NOTAS DE CREDITO'

    def __str__(self):
        return self.voucher_number


class CreditNoteDetailModel(NestedModel):

    id: AutoField = None
    fk_credit_note: ForeignKey = None
    fk_product: ForeignKey = None
    quantity: DecimalField = None
    price: DecimalField = None

    id = AutoField('ID', primary_key=True)
    fk_credit_note = ForeignKey(
        'business.CreditNoteModel', on_delete=CASCADE, verbose_name='Nota de Credito')
    fk_product = ForeignKey(
        'products.ProductModel', on_delete=CASCADE, verbose_name='Producto')
    quantity = DecimalField(
        'Cantidad', max_digits=11, decimal_places=2)
    price = DecimalField(
        'Precio', max_digits=11, decimal_places=2)

    class Meta:
        db_table = 'APIS_CREDIT_NOTE_DETAIL'
        verbose_name = 'DETALLE DE NOTA DE CREDITO'
        verbose_name_plural = 'DETALLE DE NOTAS DE CREDITO'

    def __str__(self):
        return self.fk_credit_note


class SaleModel(NestedModel):

    id: AutoField = None
    fk_client: ForeignKey = None
    fk_sale_voucher_type: ForeignKey = None
    establishment: CharField = None
    sale_billing_number: CharField = None
    voucher_number: CharField = None
    date: DateField = None
    tax: DecimalField = None
    total: DecimalField = None
    fk_way_to_pay: ForeignKey = None
    fk_user_employee: ForeignKey = None

    id = AutoField('ID', primary_key=True)
    fk_client = ForeignKey(
        'clients.ClientModel', on_delete=CASCADE, verbose_name='Cliente')
    fk_sale_voucher_type = ForeignKey(
        'business.VoucherTypeModel', on_delete=CASCADE, verbose_name='Tipo de Comprobante')
    establishment = CharField(
        'Numero de establecimiento', max_length=50)
    sale_billing_number = CharField('Numero de Libretin', max_length=50)
    voucher_number = CharField(
        'Numero de Comprobante', max_length=100)
    date = DateField('Fecha')
    tax = DecimalField('IVA', max_digits=11, decimal_places=2)
    total = DecimalField('Total', max_digits=11, decimal_places=2)
    fk_way_to_pay = ForeignKey(
        'business.WayToPayModel', on_delete=CASCADE, verbose_name='Forma de Pago')
    fk_user_employee = ForeignKey(
        'users.UserEmployeeModel', on_delete=CASCADE, verbose_name='Usuario')

    class Meta:
        db_table = 'APIS_SALE'
        verbose_name = 'FACTURA'
        verbose_name_plural = 'FACTURAS'

    def __str__(self):
        return self.fk_client


class SaleDetailModel(NestedModel):

    id: AutoField = None
    fk_sale: ForeignKey = None
    fk_product: ForeignKey = None
    quantity: DecimalField = None
    price: DecimalField = None

    id = AutoField('ID', primary_key=True)
    fk_sale = ForeignKey(
        'business.SaleModel', on_delete=CASCADE, verbose_name='Factura')
    fk_product = ForeignKey(
        'products.ProductModel', on_delete=CASCADE, verbose_name='Producto')
    quantity = DecimalField(
        'Cantidad', max_digits=11, decimal_places=2)
    price = DecimalField(
        'Precio', max_digits=11, decimal_places=2)

    class Meta:
        db_table = 'APIS_SALE_DETAIL'
        verbose_name = 'DETALLE DE FACTURA'
        verbose_name_plural = 'DETALLE DE FACTURAS'

    def __str__(self):
        return self.fk_sale
