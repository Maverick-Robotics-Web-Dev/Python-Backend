from django.db import models

class CreditNote(models.Model):
    credit_note_id = models.AutoField(primary_key=True)
    client = models.ForeignKey('Client', models.DO_NOTHING)
    credit_note_voucher_number = models.CharField(max_length=100)
    credit_note_date = models.DateField()
    credit_note_total = models.DecimalField(max_digits=11, decimal_places=0)
    user_employee = models.ForeignKey('UserEmployee', models.DO_NOTHING)
    credit_note_status = models.IntegerField()
    credit_note_description = models.CharField(max_length=256, blank=True, null=True)
    credit_note_create_at = models.DateTimeField()

    class Meta:
        db_table = 'CREDIT_NOTE'
        verbose_name = 'NOTA DE CREDITO'
        verbose_name_plural = 'NOTAS DE CREDITO'


class CreditNoteDetail(models.Model):
    credit_note_detail_id = models.AutoField(primary_key=True)
    credit_note = models.ForeignKey(CreditNote, models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    credit_note_detail_quantity = models.DecimalField(max_digits=11, decimal_places=2)
    credit_note_detail_price = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        db_table = 'CREDIT_NOTE_DETAIL'
        verbose_name = 'DETALLE DE NOTA DE CREDITO'
        verbose_name_plural = 'DETALLE DE NOTAS DE CREDITO'


class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    client = models.ForeignKey('Client', models.DO_NOTHING)
    sale_voucher_type = models.CharField(max_length=256)
    sale_establishment = models.CharField(max_length=50)
    sale_billing_number = models.CharField(max_length=50)
    sale_voucher_number = models.CharField(max_length=100)
    sale_date = models.DateField()
    sale_tax = models.DecimalField(max_digits=11, decimal_places=2)
    sale_total = models.DecimalField(max_digits=11, decimal_places=2)
    way_to_pay = models.ForeignKey('WayToPay', models.DO_NOTHING)
    user_employee = models.ForeignKey('UserEmployee', models.DO_NOTHING)
    sale_status = models.IntegerField()
    sale_status_description = models.CharField(max_length=256, blank=True, null=True)
    sale_create_at = models.DateTimeField()

    class Meta:
        db_table = 'SALE'
        verbose_name = 'FACTURA'
        verbose_name_plural = 'FACTURAS'


class SaleDetail(models.Model):
    sale_detail_id = models.AutoField(primary_key=True)
    sale = models.ForeignKey('Sale', models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    sale_detail_quantity = models.DecimalField(max_digits=11, decimal_places=2)
    sale_detail_price = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        db_table = 'SALE_DETAIL'
        verbose_name = 'DETALLE DE FACTURA'
        verbose_name_plural = 'DETALLE DE FACTURAS'


class WayToPay(models.Model):
    way_to_pay_id = models.AutoField(primary_key=True)
    way_to_pay_name = models.CharField(max_length=100)
    way_to_pay_description = models.CharField(max_length=256, blank=True, null=True)
    way_to_pay_create_at = models.DateTimeField()
    way_to_pay_update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'WAY_TO_PAY'
        verbose_name = 'FORMA DE PAGO'
        verbose_name_plural = 'FORMAS DE PAGO'