# Generated by Django 5.0.2 on 2024-04-08 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OwnCheckModel',
            fields=[
                ('create_at', models.DateTimeField(verbose_name='Fecha de Creación')),
                ('update_at', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Actualización')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(verbose_name='Fecha de Pago')),
                ('beneficiary', models.CharField(max_length=500, verbose_name='Beneficiario')),
                ('detail', models.CharField(max_length=500, verbose_name='Detalle')),
                ('voucher_type', models.CharField(max_length=50, verbose_name='Tipo de Comprobante')),
                ('voucher_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Numero de Comprobante')),
                ('deposit_date', models.DateField(verbose_name='Fecha de Deposito')),
                ('bank', models.CharField(max_length=256, verbose_name='Banco')),
                ('account_number', models.CharField(max_length=256, verbose_name='Numero de Cuenta')),
                ('check_number', models.CharField(max_length=100, verbose_name='Cheque Numero')),
                ('check_owner', models.CharField(max_length=256, verbose_name='Propietario')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Monto')),
                ('status', models.CharField(max_length=50, verbose_name='Estado')),
                ('remark', models.CharField(blank=True, max_length=500, null=True, verbose_name='Observaciones')),
            ],
            options={
                'verbose_name': 'CHEQUE PROPIO',
                'verbose_name_plural': 'CHEQUES PROPIOS',
                'db_table': 'APIS_OWN_CHECK',
            },
        ),
    ]
