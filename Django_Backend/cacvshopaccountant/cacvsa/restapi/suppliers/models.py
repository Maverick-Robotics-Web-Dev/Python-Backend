from typing import Self, LiteralString

from django.db.models import (
    Model,
    CASCADE,
    AutoField,
    CharField,
    ForeignKey,
    DateField,
    DecimalField
)

from restapi.abstracts.models import (
    NestedSupplierModel,
    NestedModel,
)


class SupplierModel(NestedSupplierModel):

    id: AutoField = None
    code: CharField = None
    business_name: CharField = None
    tradename: CharField = None
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
    code = CharField('Codigo de Proveedor', max_length=50)
    business_name = CharField('Nombre Comercial', max_length=500)
    tradename = CharField('Nombre Comercial', max_length=500, blank=True, null=True)
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

        db_table = 'APIS_SUPPLIER'
        verbose_name = 'PROVEEDOR'
        verbose_name_plural = 'PROVEEDORES'

    def __str__(self: Self) -> LiteralString:
        return self.business_name


class IncomeModel(NestedModel):

    id: AutoField = None
    fk_supplier: ForeignKey = None
    voucher_type: CharField = None
    voucher_number: CharField = None
    income_date: DateField = None
    tax_percentage: DecimalField = None
    tax: DecimalField = None
    total: DecimalField = None
    fk_user_employee: ForeignKey = None

    id = AutoField('ID', primary_key=True)
    fk_supplier = ForeignKey('suppliers.SupplierModel', on_delete=CASCADE, verbose_name='Proveedor')
    voucher_type = CharField('Tipo de Comprobate', max_length=256)
    voucher_number = CharField('Numero de Comprobante', max_length=100)
    income_date = DateField('Fecha de Ingreso')
    tax_percentage = DecimalField('Porcentaje IVA', max_digits=11, decimal_places=2)
    tax = DecimalField('IVA', max_digits=11, decimal_places=2)
    total = DecimalField('Total', max_digits=11, decimal_places=2)
    fk_user_employee = ForeignKey('users.UserEmployeeModel', on_delete=CASCADE, verbose_name='Usuario')

    class Meta:

        db_table: str = None
        verbose_name: str = None
        verbose_name_plural: str = None

        db_table = 'APIS_INCOME'
        verbose_name = 'INGRESO'
        verbose_name_plural = 'INGRESOS'

    def __str__(self: Self) -> LiteralString:
        return self.fk_supplier


class IncomeDetailModel(NestedModel):

    id: AutoField = None
    fk_income: ForeignKey = None
    fk_product: ForeignKey = None
    quantity: DecimalField = None
    purchase_price: DecimalField = None
    sale_price: DecimalField = None

    id = AutoField('ID', primary_key=True)
    fk_income = ForeignKey('suppliers.IncomeModel', on_delete=CASCADE, verbose_name='Ingreso')
    fk_product = ForeignKey('products.ProductModel', on_delete=CASCADE, verbose_name='Producto')
    quantity = DecimalField('Cantidad', max_digits=11, decimal_places=2)
    purchase_price = DecimalField('Precio de Compra', max_digits=11, decimal_places=2)
    sale_price = DecimalField('Precio de Venta', max_digits=11, decimal_places=2)

    class Meta:

        db_table: str = None
        verbose_name: str = None
        verbose_name_plural: str = None

        db_table = 'APIS_INCOME_DETAIL'
        verbose_name = 'DETALLE DE INGRESO'
        verbose_name_plural = 'DETALLES DE INGRESO'

    def __str__(self: Self) -> LiteralString:
        return self.fk_income
