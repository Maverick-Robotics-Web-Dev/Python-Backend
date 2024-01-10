from django.db import models

class CategoryModel(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_code = models.CharField('Codigo de Categoria',max_length=50)
    category_name = models.CharField('Nombre',max_length=50)
    category_description = models.CharField('Descripción',max_length=256, default='Ninguna')
    category_img = models.CharField('Imagen',max_length=256)
    category_status = models.CharField('Estado', max_length=50)
    category_status_description = models.CharField('Descripción',max_length=256, default='Ninguna')
    fk_user_employee = models.ForeignKey('users.UserEmployeeModel', on_delete=models.CASCADE)
    category_create_at = models.DateTimeField('Fecha de Creación')
    category_update_at = models.DateTimeField('Fecha de Actualización',blank=True, null=True)

    class Meta:
        db_table = 'APIS_CATEGORY'
        verbose_name = 'CATEGORIA'
        verbose_name_plural = 'CATEGORIAS'


class BrandModel(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_code = models.CharField('Codigo de Marca',max_length=50)
    brand_name = models.CharField('Nombre',max_length=50)
    brand_description = models.CharField('Descripción', max_length=256, default='Ninguna')
    brand_img = models.CharField('Imagen',max_length=256)
    brand_status = models.CharField('Estado', max_length=50)
    brand_status_description = models.CharField('Descripción', max_length=256, default='Ninguna')
    fk_user_employee = models.ForeignKey('users.UserEmployeeModel', on_delete=models.CASCADE)
    brand_create_at = models.DateTimeField('Fecha de Creación')
    brand_update_at = models.DateTimeField('Fecha de Actualización',blank=True, null=True)

    class Meta:
        db_table = 'APIS_BRAND'
        verbose_name = 'MARCA'
        verbose_name_plural = 'MARCAS'


class ProductModel(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_barcode = models.CharField('Codigo de Barras',max_length=13, default='No posee codigo')
    product_code = models.CharField('Codigo de Producto',max_length=50)
    product_name = models.CharField('Nombre',max_length=100)
    product_stock = models.IntegerField('Stock')
    product_presentation = models.CharField('Presentación',max_length=256)
    product_purchase_price = models.DecimalField('Precio de Compra',max_digits=11, decimal_places=2)
    product_sale_price = models.DecimalField('Precio de Venta',max_digits=11, decimal_places=2)
    product_number_sale = models.PositiveBigIntegerField('Numero de Ventas',default=0)
    product_img = models.CharField('Imagen',max_length=256)
    product_due_date = models.DateField('Fecha de Vencimiento',blank=True, null=True)
    fk_supplier = models.ForeignKey('suppliers.SupplierModel', on_delete=models.CASCADE)
    fk_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    fk_brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    product_description = models.CharField('Descripción',max_length=256, default='Ninguna')
    fk_user_employee = models.ForeignKey('users.UserEmployeeModel', on_delete=models.CASCADE)
    product_status = models.CharField('Estado', max_length=50)
    product_status_description = models.CharField('Descripción',max_length=256, blank=True, null=True)
    product_create_at = models.DateTimeField('Fecha de Creación')
    product_update_at = models.DateTimeField('Fecha de Actualización',blank=True, null=True)

    class Meta:
        db_table = 'APIS_PRODUCT'
        verbose_name = 'PRODUCTO'
        verbose_name_plural = 'PRODUCTOS'
