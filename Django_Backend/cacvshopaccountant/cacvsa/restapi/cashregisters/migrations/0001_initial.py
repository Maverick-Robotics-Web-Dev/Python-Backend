# Generated by Django 5.0.1 on 2024-02-08 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CashRegisterClosingModel',
            fields=[
                ('cash_register_closing_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('cash_register_closing_date', models.DateTimeField(verbose_name='Fecha')),
                ('cash_register_closing_total_voucher_transactions', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Total de Ventas')),
                ('cash_register_closing_total_cash_equivalent', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Total Transferencias')),
                ('cash_register_closing_total_cash', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Total en Efectivo')),
                ('cash_register_closing_missing_or_surplus', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Faltante o Excedente')),
                ('cash_register_closing_amount', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Monto de Cierre')),
                ('cash_register_closing_remark', models.CharField(default='Ninguna', max_length=1024, verbose_name='Observación')),
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
                ('cash_register_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('cash_register_number', models.CharField(max_length=256, verbose_name='Caja')),
                ('cash_register_status', models.CharField(max_length=50, verbose_name='Estado')),
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
                ('cash_register_movements_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('cash_register_movements_date', models.DateTimeField(verbose_name='Fecha')),
                ('cash_register_movements_detail', models.CharField(max_length=500, verbose_name='Detalle')),
                ('cash_register_movements_type', models.CharField(max_length=100, verbose_name='Tipo')),
                ('cash_register_movements_amount', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Monto')),
                ('cash_register_movements_created_at', models.DateTimeField(verbose_name='Fecha de Creación')),
                ('cash_register_movements_update_at', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Actualización')),
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
                ('cash_register_opening_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('cash_register_opening_date', models.DateTimeField(verbose_name='Fecha')),
                ('cash_register_opening_amount', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Monto de Apertura')),
            ],
            options={
                'verbose_name': 'APERTURA DE CAJA REGISTRADORA',
                'verbose_name_plural': 'APERTURAS DE CAJA REGISTRADORA',
                'db_table': 'APIS_CASH_REGISTER_OPENING',
            },
        ),
    ]
