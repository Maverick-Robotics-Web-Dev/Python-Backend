# Generated by Django 5.0.1 on 2024-02-01 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandModel',
            fields=[
                ('brand_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_code', models.CharField(max_length=50, verbose_name='Codigo de Marca')),
                ('brand_name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('brand_description', models.CharField(default='Ninguna', max_length=256, verbose_name='Descripción')),
                ('brand_img', models.CharField(max_length=256, verbose_name='Imagen')),
                ('brand_status', models.CharField(max_length=50, verbose_name='Estado')),
                ('brand_status_description', models.CharField(default='Ninguna', max_length=256, verbose_name='Descripción')),
                ('brand_create_at', models.DateTimeField(verbose_name='Fecha de Creación')),
                ('brand_update_at', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Actualización')),
            ],
            options={
                'verbose_name': 'MARCA',
                'verbose_name_plural': 'MARCAS',
                'db_table': 'APIS_BRAND',
            },
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('category_code', models.CharField(max_length=50, verbose_name='Codigo de Categoria')),
                ('category_name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('category_description', models.CharField(default='Ninguna', max_length=256, verbose_name='Descripción')),
                ('category_img', models.CharField(max_length=256, verbose_name='Imagen')),
                ('category_status', models.CharField(max_length=50, verbose_name='Estado')),
                ('category_status_description', models.CharField(default='Ninguna', max_length=256, verbose_name='Descripción')),
                ('category_create_at', models.DateTimeField(verbose_name='Fecha de Creación')),
                ('category_update_at', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Actualización')),
            ],
            options={
                'verbose_name': 'CATEGORIA',
                'verbose_name_plural': 'CATEGORIAS',
                'db_table': 'APIS_CATEGORY',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('product_barcode', models.CharField(default='No posee codigo', max_length=13, verbose_name='Codigo de Barras')),
                ('product_code', models.CharField(max_length=50, verbose_name='Codigo de Producto')),
                ('product_name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('product_stock', models.IntegerField(verbose_name='Stock')),
                ('product_presentation', models.CharField(max_length=256, verbose_name='Presentación')),
                ('product_purchase_price', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Precio de Compra')),
                ('product_sale_price', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Precio de Venta')),
                ('product_number_sale', models.PositiveBigIntegerField(default=0, verbose_name='Numero de Ventas')),
                ('product_img', models.CharField(max_length=256, verbose_name='Imagen')),
                ('product_due_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Vencimiento')),
                ('product_description', models.CharField(default='Ninguna', max_length=256, verbose_name='Descripción')),
                ('product_status', models.CharField(max_length=50, verbose_name='Estado')),
                ('product_status_description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Descripción')),
                ('product_create_at', models.DateTimeField(verbose_name='Fecha de Creación')),
                ('product_update_at', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Actualización')),
            ],
            options={
                'verbose_name': 'PRODUCTO',
                'verbose_name_plural': 'PRODUCTOS',
                'db_table': 'APIS_PRODUCT',
            },
        ),
    ]
