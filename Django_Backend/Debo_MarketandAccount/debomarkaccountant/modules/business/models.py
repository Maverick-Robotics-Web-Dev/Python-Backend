from django.db import models

class CreditNote(models.Model):
    credit_note_id = models.AutoField(primary_key=True)
    # client = models.ForeignKey('Client', on_delete=models.CASCADE)
    credit_note_voucher_number = models.CharField(max_length=100)
    credit_note_date = models.DateField()
    credit_note_total = models.DecimalField(max_digits=11, decimal_places=0)
    # user_employee = models.ForeignKey('UserEmployee', on_delete=models.CASCADE)
    credit_note_status = models.IntegerField()
    credit_note_description = models.CharField(max_length=256, blank=True, null=True)
    credit_note_create_at = models.DateTimeField()

    class Meta:
        db_table = 'CREDIT_NOTE'
        verbose_name = 'NOTA DE CREDITO'
        verbose_name_plural = 'NOTAS DE CREDITO'


class CreditNoteDetail(models.Model):
    credit_note_detail_id = models.AutoField(primary_key=True)
    # credit_note = models.ForeignKey(CreditNote, on_delete=models.CASCADE)
    # product = models.ForeignKey('Product', on_delete=models.CASCADE)
    credit_note_detail_quantity = models.DecimalField(max_digits=11, decimal_places=2)
    credit_note_detail_price = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        db_table = 'CREDIT_NOTE_DETAIL'
        verbose_name = 'DETALLE DE NOTA DE CREDITO'
        verbose_name_plural = 'DETALLE DE NOTAS DE CREDITO'


class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    # client = models.ForeignKey('Client', on_delete=models.CASCADE)
    sale_voucher_type = models.CharField(max_length=256)
    sale_establishment = models.CharField(max_length=50)
    sale_billing_number = models.CharField(max_length=50)
    sale_voucher_number = models.CharField(max_length=100)
    sale_date = models.DateField()
    sale_tax = models.DecimalField(max_digits=11, decimal_places=2)
    sale_total = models.DecimalField(max_digits=11, decimal_places=2)
    # way_to_pay = models.ForeignKey('WayToPay', on_delete=models.CASCADE)
    # user_employee = models.ForeignKey('UserEmployee', on_delete=models.CASCADE)
    sale_status = models.IntegerField()
    sale_status_description = models.CharField(max_length=256, blank=True, null=True)
    sale_create_at = models.DateTimeField()

    class Meta:
        db_table = 'SALE'
        verbose_name = 'FACTURA'
        verbose_name_plural = 'FACTURAS'


class SaleDetail(models.Model):
    sale_detail_id = models.AutoField(primary_key=True)
    # sale = models.ForeignKey('Sale', on_delete=models.CASCADE)
    # product = models.ForeignKey('Product', on_delete=models.CASCADE)
    sale_detail_quantity = models.DecimalField(max_digits=11, decimal_places=2)
    sale_detail_price = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        db_table = 'SALE_DETAIL'
        verbose_name = 'DETALLE DE FACTURA'
        verbose_name_plural = 'DETALLE DE FACTURAS'


class WayToPay(models.Model):
    way_to_pay_id = models.AutoField(primary_key=True)
    way_to_pay_name = models.CharField('Forma de Pago',max_length=100)
    way_to_pay_description = models.CharField('Descripcion',max_length=256, blank=True, null=True)
    way_to_pay_create_at = models.DateTimeField('Fecha de Creación')
    way_to_pay_update_at = models.DateTimeField('Fecha de Actualización',blank=True, null=True)

    class Meta:
        db_table = 'WAY_TO_PAY'
        verbose_name = 'FORMA DE PAGO'
        verbose_name_plural = 'FORMAS DE PAGO'
