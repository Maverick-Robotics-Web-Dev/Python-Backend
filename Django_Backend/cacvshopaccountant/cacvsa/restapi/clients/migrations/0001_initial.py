# Generated by Django 5.0.2 on 2024-03-18 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientCheckModel',
            fields=[
                ('client_check_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('client_check_date_admission', models.DateField(verbose_name='Fecha de Admisión')),
                ('client_check_detail', models.CharField(max_length=500, verbose_name='Detalle')),
                ('client_check_voucher_type', models.CharField(max_length=256, verbose_name='Tipo de Comprobante')),
                ('client_check_voucher_number', models.CharField(max_length=100, verbose_name='Numero del Comprobante')),
                ('client_check_deposit_date', models.DateField(verbose_name='Fecha de Deposito')),
                ('client_check_bank', models.CharField(max_length=256, verbose_name='Banco')),
                ('client_check_account_number', models.CharField(max_length=256, verbose_name='Numero de Cuenta')),
                ('client_check_number', models.CharField(max_length=100, verbose_name='Numero de Cheque')),
                ('client_check_owner', models.CharField(max_length=256, verbose_name='Propietario de la Cuenta')),
                ('client_check_amount', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Monto')),
                ('client_check_status', models.CharField(max_length=50, verbose_name='Estado')),
                ('client_check_deposited_in', models.CharField(blank=True, max_length=256, null=True, verbose_name='Depositado en Banco')),
                ('client_check_deposit_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Numero de Comprobante')),
                ('client_check_endorsement_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Endoso')),
                ('client_check_discharge_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Descargo')),
                ('client_check_beneficiary', models.CharField(blank=True, max_length=500, null=True, verbose_name='Beneficiario')),
                ('client_check_remark', models.CharField(default='Ninguna', max_length=500, verbose_name='Observaciones')),
                ('client_check_create_at', models.DateTimeField(verbose_name='Fecha de Creación')),
                ('client_check_upgrade_at', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Actualizacion')),
            ],
            options={
                'verbose_name': 'CHEQUE DEL CLIENTE',
                'verbose_name_plural': 'CHEQUES DEL CLIENTE',
                'db_table': 'APIS_CLIENT_CHECK',
            },
        ),
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('document_type', models.CharField(max_length=20, verbose_name='Tipo de Documento')),
                ('document_number', models.PositiveIntegerField(verbose_name='Numero')),
                ('lastname', models.CharField(max_length=500, verbose_name='Apellidos')),
                ('name', models.CharField(max_length=500, verbose_name='Nombres')),
                ('country', models.CharField(max_length=200, verbose_name='Pais')),
                ('state_province', models.CharField(max_length=200, verbose_name='Provincia o Estado')),
                ('city', models.CharField(max_length=200, verbose_name='Ciudad')),
                ('address', models.CharField(max_length=200, verbose_name='Dirección')),
                ('postal_code', models.CharField(default='S/N', max_length=200, verbose_name='Codigo Postal')),
                ('phone_number', models.CharField(default='Sin Telefono Convencional', max_length=50, verbose_name='Telefono')),
                ('cellphone_number', models.CharField(max_length=50, verbose_name='Celular')),
                ('email', models.CharField(default='No Posee email', max_length=100, verbose_name='E-mail')),
                ('img', models.ImageField(blank=True, null=True, upload_to='persons/', verbose_name='Imagen')),
                ('client_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('client_code', models.CharField(max_length=50, verbose_name='Codigo de Cliente')),
                ('client_trade_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Nombre Comercial')),
                ('client_branch_office_address_one', models.CharField(default='Sin Sucursal', max_length=200, verbose_name='Dirección')),
                ('client_branch_office_address_two', models.CharField(default='Sin Sucursal', max_length=200, verbose_name='Dirección')),
                ('client_branch_office_address_three', models.CharField(default='Sin Sucursal', max_length=200, verbose_name='Dirección')),
                ('client_branch_office_address_four', models.CharField(default='Sin Sucursal', max_length=200, verbose_name='Dirección')),
                ('client_phone_number_one', models.CharField(default='No posee numero telefonico', max_length=50, verbose_name='Telefono')),
                ('client_phone_number_two', models.CharField(default='No posee numero telefonico', max_length=50, verbose_name='Telefono')),
                ('client_phone_number_three', models.CharField(default='No posee numero telefonico', max_length=50, verbose_name='Telefono')),
                ('client_phone_number_four', models.CharField(default='No posee numero telefonico', max_length=50, verbose_name='Telefono')),
                ('client_status', models.BooleanField(default=False, verbose_name='Estado')),
                ('client_status_description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Descripción')),
                ('client_create_at', models.DateTimeField(verbose_name='Fecha de Creación')),
                ('client_upgrade_at', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Actulización')),
            ],
            options={
                'verbose_name': 'CLIENTE',
                'verbose_name_plural': 'CLIENTES',
                'db_table': 'APIS_CLIENT',
            },
        ),
    ]
