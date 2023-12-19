from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_code = models.CharField(max_length=50)
    category_name = models.CharField(max_length=50)
    category_description = models.CharField(
        max_length=256, blank=True, null=True)
    category_img = models.CharField(max_length=256)
    category_status = models.IntegerField()
    category_status_description = models.CharField(
        max_length=256, blank=True, null=True)
    user_employee = models.ForeignKey('UserEmployee', on_delete=models.CASCADE)
    category_create_at = models.DateTimeField()
    category_update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'CATEGORY'
        verbose_name = 'CATEGORIA'
        verbose_name_plural = 'CATEGORIAS'


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_code = models.CharField(max_length=50)
    brand_name = models.CharField(max_length=50)
    brand_description = models.CharField(
        max_length=256, blank=True, null=True)
    brand_img = models.CharField(max_length=256)
    brand_status = models.IntegerField()
    brand_status_description = models.CharField(
        max_length=256, blank=True, null=True)
    user_employee = models.ForeignKey('UserEmployee', on_delete=models.CASCADE)
    brand_create_at = models.DateTimeField()
    brand_update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'BRAND'
        verbose_name = 'MARCA'
        verbose_name_plural = 'MARCAS'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_barcode = models.CharField(max_length=13, unique=True)
    product_code = models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)
    product_barcode = models.CharField(max_length=50, blank=True, null=True)
    product_stock = models.IntegerField()
    product_presentation = models.CharField(max_length=256)
    product_price_in = models.DecimalField(max_digits=11, decimal_places=2)
    product_price_out = models.DecimalField(max_digits=11, decimal_places=2)
    product_number_sale = models.PositiveBigIntegerField(default=0)
    product_img = models.CharField(max_length=256)
    product_due_date = models.DateField(blank=True, null=True)
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    product_description = models.CharField(
        max_length=256, blank=True, null=True)
    user_employee = models.ForeignKey('UserEmployee', on_delete=models.CASCADE)
    product_status = models.IntegerField()
    product_status_description = models.CharField(
        max_length=256, blank=True, null=True)
    product_create_at = models.DateTimeField()
    product_update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'PRODUCT'
        verbose_name = 'PRODUCTO'
        verbose_name_plural = 'PRODUCTOS'
