# Generated by Django 5.0.2 on 2024-04-03 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CashRegisterClosingModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('closing_date', models.DateTimeField(verbose_name='Fecha de Cierre')),
                ('total_sales', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Total de Ventas')),
                ('total_transfers', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Total Transferencias')),
                ('total_cash', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Total en Efectivo')),
                ('missing_or_surplus', models.DecimalField(decimal_places=2, default=0.0, max_digits=11, verbose_name='Faltante o Excedente')),
                ('closing_amount', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Monto de Cierre')),
                ('remark', models.CharField(default='Ninguna', max_length=1024, verbose_name='Observación')),
            ],
            options={
                'verbose_name': 'CIERRE DE CAJA REGISTRADORA',
                'verbose_name_plural': 'CIERRES DE CAJA REGISTRADORA',
                'db_table': 'APIS_CASH_REGISTER_CLOSING',
            },
        ),
        migrations.CreateModel(
            name='CashRegisterModel',
            fields=[
                ('status', models.BooleanField(default=False, verbose_name='Estado')),
                ('status_description', models.CharField(default='No existe descripción', max_length=256, verbose_name='Descripción del Estado')),
                ('create_at', models.DateTimeField(verbose_name='Fecha de Creación')),
                ('update_at', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Actualización')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=256, verbose_name='Caja')),
                ('condition', models.BooleanField(verbose_name='Condición')),
            ],
            options={
                'verbose_name': 'CAJA REGISTRADORA',
                'verbose_name_plural': 'CAJAS REGISTRADORAS',
                'db_table': 'APIS_CASH_REGISTER',
            },
        ),
        migrations.CreateModel(
            name='CashRegisterMovementsModel',
            fields=[
                ('status', models.BooleanField(default=False, verbose_name='Estado')),
                ('status_description', models.CharField(default='No existe descripción', max_length=256, verbose_name='Descripción del Estado')),
                ('create_at', models.DateTimeField(verbose_name='Fecha de Creación')),
                ('update_at', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Actualización')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('movements_date', models.DateTimeField(verbose_name='Fecha de Movimiento')),
                ('movements_detail', models.CharField(max_length=500, verbose_name='Detalle')),
                ('movements_type', models.CharField(max_length=100, verbose_name='Tipo')),
                ('movements_amount', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Monto')),
            ],
            options={
                'verbose_name': 'MOVIMIENTO DE CAJA REGISTRADORA',
                'verbose_name_plural': 'MOVIMIENTOS DE CAJA REGISTRADORA',
                'db_table': 'APIS_CASH_REGISTER_MOVEMENTS',
            },
        ),
        migrations.CreateModel(
            name='CashRegisterOpeningModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('opening_date', models.DateTimeField(verbose_name='Fecha de Apertura')),
                ('opening_amount', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Monto de Apertura')),
                ('missing_or_surplus', models.DecimalField(decimal_places=2, default=0.0, max_digits=11, verbose_name='Faltante o Excedente')),
            ],
            options={
                'verbose_name': 'APERTURA DE CAJA REGISTRADORA',
                'verbose_name_plural': 'APERTURAS DE CAJA REGISTRADORA',
                'db_table': 'APIS_CASH_REGISTER_OPENING',
            },
        ),
    ]
