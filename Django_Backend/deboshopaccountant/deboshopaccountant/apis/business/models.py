from django.db import models

class WayToPayModel(models.Model):
    way_to_pay_id = models.AutoField(primary_key=True)
    way_to_pay_name = models.CharField('Forma de Pago',max_length=100)
    way_to_pay_description = models.CharField('Descripcion',max_length=256, blank=True, null=True)
    way_to_pay_create_at = models.DateTimeField('Fecha de Creación')
    way_to_pay_update_at = models.DateTimeField('Fecha de Actualización',blank=True, null=True)

    class Meta:
        db_table = 'WAY_TO_PAY'
        verbose_name = 'FORMA DE PAGO'
        verbose_name_plural = 'FORMAS DE PAGO'

class VoucherTypeModel(models.Model):
    voucher_type_id = models.AutoField(primary_key=True)
    voucher_type_name = models.CharField('Tipo de Comprobante', max_length=100)
    voucher_type_description = models.CharField('Descripción', max_length=256, default='No existe descripción')
    voucher_type_create_at = models.DateTimeField('Fecha de Creación')
    voucher_type_update_at = models.DateTimeField('Fecha de Actualización', blank=True, null=True)

    class Meta:
        db_table = 'VOUCHER_TYPE'
        verbose_name = 'TIPO DE COMPROBANTE'
        verbose_name_plural = 'TIPOS DE COMPROBANTE'

class CreditNoteModel(models.Model):
    credit_note_id = models.AutoField(primary_key=True)
    fk_client = models.ForeignKey('clients.ClientModel', on_delete=models.CASCADE)
    credit_note_voucher_number = models.CharField('Numero de Comprobante',max_length=100)
    credit_note_date = models.DateField('Fecha')
    credit_note_total = models.DecimalField('Total',max_digits=11, decimal_places=0)
    fk_user_employee = models.ForeignKey('users.UserEmployeeModel', on_delete=models.CASCADE)
    credit_note_status = models.CharField('Estado', max_length=50)
    credit_note_description = models.CharField('Descripción',max_length=256, blank=True, null=True)
    credit_note_create_at = models.DateTimeField('Fecha de Creación')

    class Meta:
        db_table = 'CREDIT_NOTE'
        verbose_name = 'NOTA DE CREDITO'
        verbose_name_plural = 'NOTAS DE CREDITO'


class CreditNoteDetailModel(models.Model):
    credit_note_detail_id = models.AutoField(primary_key=True)
    fk_credit_note = models.ForeignKey(CreditNoteModel, on_delete=models.CASCADE)
    fk_product = models.ForeignKey('products.ProductModel', on_delete=models.CASCADE)
    credit_note_detail_quantity = models.DecimalField('Cantidad',max_digits=11, decimal_places=2)
    credit_note_detail_price = models.DecimalField('Precio',max_digits=11, decimal_places=2)

    class Meta:
        db_table = 'CREDIT_NOTE_DETAIL'
        verbose_name = 'DETALLE DE NOTA DE CREDITO'
        verbose_name_plural = 'DETALLE DE NOTAS DE CREDITO'


class SaleModel(models.Model):
    sale_id = models.AutoField(primary_key=True)
    fk_client = models.ForeignKey('clients.ClientModel', on_delete=models.CASCADE)
    fk_sale_voucher_type = models.ForeignKey(VoucherTypeModel, on_delete=models.CASCADE)
    sale_establishment = models.CharField('Numero de establecimiento',max_length=50)
    sale_billing_number = models.CharField('Numero de Libretin',max_length=50)
    sale_voucher_number = models.CharField('Numero de Comprobante',max_length=100)
    sale_date = models.DateField('Fecha')
    sale_tax = models.DecimalField('IVA',max_digits=11, decimal_places=2)
    sale_total = models.DecimalField('Total',max_digits=11, decimal_places=2)
    fk_way_to_pay = models.ForeignKey(WayToPayModel, on_delete=models.CASCADE)
    fk_user_employee = models.ForeignKey('users.UserEmployeeModel', on_delete=models.CASCADE)
    sale_status = models.CharField('Estado', max_length=50)
    sale_status_description = models.CharField('Descripción',max_length=256, blank=True, null=True)
    sale_create_at = models.DateTimeField('Fecha de Creación')

    class Meta:
        db_table = 'SALE'
        verbose_name = 'FACTURA'
        verbose_name_plural = 'FACTURAS'


class SaleDetailModel(models.Model):
    sale_detail_id = models.AutoField(primary_key=True)
    fk_sale = models.ForeignKey(SaleModel, on_delete=models.CASCADE)
    fk_product = models.ForeignKey('products.ProductModel', on_delete=models.CASCADE)
    sale_detail_quantity = models.DecimalField('Cantidad',max_digits=11, decimal_places=2)
    sale_detail_price = models.DecimalField('Precio',max_digits=11, decimal_places=2)

    class Meta:
        db_table = 'SALE_DETAIL'
        verbose_name = 'DETALLE DE FACTURA'
        verbose_name_plural = 'DETALLE DE FACTURAS'
