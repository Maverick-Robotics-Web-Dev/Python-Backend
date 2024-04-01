from typing import Self, LiteralString

from django.db.models import (
    CASCADE,
    AutoField,
    CharField,
    ForeignKey,
    DecimalField,
    PositiveBigIntegerField,
    DateField
)

from restapi.abstracts.models import NestedModel


class CategoryModel(NestedModel):

    id: AutoField = None
    code: CharField = None
    name: CharField = None
    description: CharField = None
    img: CharField = None
    fk_user_employee: ForeignKey = None

    id = AutoField('ID', primary_key=True)
    code = CharField('Codigo de Categoria', max_length=50)
    name = CharField('Nombre', max_length=50)
    description = CharField('Descripción', max_length=256, default='Ninguna')
    img = CharField('Imagen', max_length=256)
    fk_user_employee = ForeignKey('users.UserEmployeeModel', on_delete=CASCADE, verbose_name='Usuario')

    class Meta:

        db_table: str = None
        verbose_name: str = None
        verbose_name_plural: str = None

        db_table = 'APIS_CATEGORY'
        verbose_name = 'CATEGORIA'
        verbose_name_plural = 'CATEGORIAS'

    def __str__(self: Self) -> LiteralString:
        return self.name


class BrandModel(NestedModel):

    id: AutoField = None
    code: CharField = None
    name: CharField = None
    description: CharField = None
    img: CharField = None
    fk_user_employee: ForeignKey = None

    id = AutoField('ID', primary_key=True)
    code = CharField('Codigo de Marca', max_length=50)
    name = CharField('Nombre', max_length=50)
    description = CharField('Descripción', max_length=256, default='Ninguna')
    img = CharField('Imagen', max_length=256)
    fk_user_employee = ForeignKey('users.UserEmployeeModel', on_delete=CASCADE, verbose_name='Usuario')

    class Meta:

        db_table: str = None
        verbose_name: str = None
        verbose_name_plural: str = None

        db_table = 'APIS_BRAND'
        verbose_name = 'MARCA'
        verbose_name_plural = 'MARCAS'

    def __str__(self: Self) -> LiteralString:
        return self.name


class ProductModel(NestedModel):

    id: AutoField = None
    barcode: CharField = None
    code: CharField = None
    name: CharField = None
    stock: PositiveBigIntegerField = None
    presentation: CharField = None
    purchase_price: DecimalField = None
    sale_price: DecimalField = None
    number_sale: PositiveBigIntegerField = None
    img: CharField = None
    due_date: DateField = None
    fk_supplier: ForeignKey = None
    fk_category: ForeignKey = None
    fk_brand: ForeignKey = None
    description: CharField = None
    fk_user_employee: ForeignKey = None

    id = AutoField('ID', primary_key=True)
    barcode = CharField('Codigo de Barras', max_length=13, default='No posee codigo')
    code = CharField('Codigo de Producto', max_length=50)
    name = CharField('Nombre', max_length=100)
    stock = PositiveBigIntegerField('Stock')
    presentation = CharField('Presentación', max_length=256)
    purchase_price = DecimalField('Precio de Compra', max_digits=11, decimal_places=2)
    sale_price = DecimalField('Precio de Venta', max_digits=11, decimal_places=2)
    number_sale = PositiveBigIntegerField('Numero de Ventas', default=0)
    img = CharField('Imagen', max_length=256)
    due_date = DateField('Fecha de Vencimiento', blank=True, null=True)
    fk_supplier = ForeignKey('suppliers.SupplierModel', on_delete=CASCADE, verbose_name='Proveedor')
    fk_category = ForeignKey('products.CategoryModel', on_delete=CASCADE, verbose_name='Categoria')
    fk_brand = ForeignKey('products.BrandModel', on_delete=CASCADE, verbose_name='Marca')
    description = CharField('Descripción', max_length=256, default='Ninguna')
    fk_user_employee = ForeignKey('users.UserEmployeeModel', on_delete=CASCADE, verbose_name='Usuario')

    class Meta:

        db_table: str = None
        verbose_name: str = None
        verbose_name_plural: str = None

        db_table = 'APIS_PRODUCT'
        verbose_name = 'PRODUCTO'
        verbose_name_plural = 'PRODUCTOS'

    def __str__(self: Self) -> LiteralString:
        return self.name
