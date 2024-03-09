from django.db import models


class WayToPayModel(models.Model):
    way_to_pay_id = models.AutoField('ID', primary_key=True)
    way_to_pay_name = models.CharField('Forma de Pago', max_length=100)
    way_to_pay_description = models.CharField(
        'Descripcion', max_length=256, blank=True, null=True)
    fk_user_employee = models.ForeignKey(
        'users.UserEmployeeModel', on_delete=models.CASCADE, verbose_name='Usuario')
    way_to_pay_status = models.BooleanField('Estado', default=False)
    way_to_pay_status_description = models.CharField(
        'Descripción del Estado', max_length=256, blank=True, null=True)
    way_to_pay_create_at = models.DateTimeField('Fecha de Creación')
    way_to_pay_update_at = models.DateTimeField(
        'Fecha de Actualización', blank=True, null=True)

    class Meta:
        db_table = 'APIS_WAY_TO_PAY'
        verbose_name = 'FORMA DE PAGO'
        verbose_name_plural = 'FORMAS DE PAGO'

    def __str__(self):
        return self.way_to_pay_name


class VoucherTypeModel(models.Model):
    voucher_type_id = models.AutoField('ID', primary_key=True)
    voucher_type_name = models.CharField('Tipo de Comprobante', max_length=100)
    voucher_type_description = models.CharField(
        'Descripción', max_length=256, default='No existe descripción')
    fk_user_employee = models.ForeignKey(
        'users.UserEmployeeModel', on_delete=models.CASCADE, verbose_name='Usuario')
    voucher_type_status = models.BooleanField('Estado', default=False)
    voucher_type_status_description = models.CharField(
        'Descripción', max_length=256, blank=True, null=True)
    voucher_type_create_at = models.DateTimeField('Fecha de Creación')
    voucher_type_update_at = models.DateTimeField(
        'Fecha de Actualización', blank=True, null=True)

    class Meta:
        db_table = 'APIS_VOUCHER_TYPE'
        verbose_name = 'TIPO DE COMPROBANTE'
        verbose_name_plural = 'TIPOS DE COMPROBANTE'

    def __str__(self):
        return self.voucher_type_name


class CreditNoteModel(models.Model):
    credit_note_id = models.AutoField('ID', primary_key=True)
    fk_client = models.ForeignKey(
        'clients.ClientModel', on_delete=models.CASCADE, verbose_name='Cliente')
    credit_note_voucher_number = models.CharField(
        'Numero de Comprobante', max_length=100)
    credit_note_date = models.DateField('Fecha')
    credit_note_total = models.DecimalField(
        'Total', max_digits=11, decimal_places=0)
    fk_user_employee = models.ForeignKey(
        'users.UserEmployeeModel', on_delete=models.CASCADE, verbose_name='Usuario')
    credit_note_status = models.BooleanField('Estado', default=False)
    credit_note_description = models.CharField(
        'Descripción', max_length=256, blank=True, null=True)
    credit_note_create_at = models.DateTimeField('Fecha de Creación')

    class Meta:
        db_table = 'APIS_CREDIT_NOTE'
        verbose_name = 'NOTA DE CREDITO'
        verbose_name_plural = 'NOTAS DE CREDITO'

    def __str__(self):
        return self.fk_client


class CreditNoteDetailModel(models.Model):
    credit_note_detail_id = models.AutoField('ID', primary_key=True)
    fk_credit_note = models.ForeignKey(
        'business.CreditNoteModel', on_delete=models.CASCADE, verbose_name='Nota de Credito')
    fk_product = models.ForeignKey(
        'products.ProductModel', on_delete=models.CASCADE, verbose_name='Producto')
    credit_note_detail_quantity = models.DecimalField(
        'Cantidad', max_digits=11, decimal_places=2)
    credit_note_detail_price = models.DecimalField(
        'Precio', max_digits=11, decimal_places=2)

    class Meta:
        db_table = 'APIS_CREDIT_NOTE_DETAIL'
        verbose_name = 'DETALLE DE NOTA DE CREDITO'
        verbose_name_plural = 'DETALLE DE NOTAS DE CREDITO'

    def __str__(self):
        return self.fk_credit_note


class SaleModel(models.Model):
    sale_id = models.AutoField('ID', primary_key=True)
    fk_client = models.ForeignKey(
        'clients.ClientModel', on_delete=models.CASCADE, verbose_name='Cliente')
    fk_sale_voucher_type = models.ForeignKey(
        'business.VoucherTypeModel', on_delete=models.CASCADE, verbose_name='Tipo de Comprobante')
    sale_establishment = models.CharField(
        'Numero de establecimiento', max_length=50)
    sale_billing_number = models.CharField('Numero de Libretin', max_length=50)
    sale_voucher_number = models.CharField(
        'Numero de Comprobante', max_length=100)
    sale_date = models.DateField('Fecha')
    sale_tax = models.DecimalField('IVA', max_digits=11, decimal_places=2)
    sale_total = models.DecimalField('Total', max_digits=11, decimal_places=2)
    fk_way_to_pay = models.ForeignKey(
        'business.WayToPayModel', on_delete=models.CASCADE, verbose_name='Forma de Pago')
    fk_user_employee = models.ForeignKey(
        'users.UserEmployeeModel', on_delete=models.CASCADE, verbose_name='Usuario')
    sale_status = models.BooleanField('Estado', default=False)
    sale_status_description = models.CharField(
        'Descripción', max_length=256, blank=True, null=True)
    sale_create_at = models.DateTimeField('Fecha de Creación')

    class Meta:
        db_table = 'APIS_SALE'
        verbose_name = 'FACTURA'
        verbose_name_plural = 'FACTURAS'

    def __str__(self):
        return self.fk_client


class SaleDetailModel(models.Model):
    sale_detail_id = models.AutoField('ID', primary_key=True)
    fk_sale = models.ForeignKey(
        'business.SaleModel', on_delete=models.CASCADE, verbose_name='Factura')
    fk_product = models.ForeignKey(
        'products.ProductModel', on_delete=models.CASCADE, verbose_name='Producto')
    sale_detail_quantity = models.DecimalField(
        'Cantidad', max_digits=11, decimal_places=2)
    sale_detail_price = models.DecimalField(
        'Precio', max_digits=11, decimal_places=2)

    class Meta:
        db_table = 'APIS_SALE_DETAIL'
        verbose_name = 'DETALLE DE FACTURA'
        verbose_name_plural = 'DETALLE DE FACTURAS'

    def __str__(self):
        return self.fk_sale
