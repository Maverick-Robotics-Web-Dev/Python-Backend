# Generated by Django 5.0.2 on 2024-03-18 19:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0002_initial'),
        ('clients', '0001_initial'),
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='creditnotemodel',
            name='fk_user_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='creditnotedetailmodel',
            name='fk_credit_note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.creditnotemodel', verbose_name='Nota de Credito'),
        ),
        migrations.AddField(
            model_name='saledetailmodel',
            name='fk_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productmodel', verbose_name='Producto'),
        ),
        migrations.AddField(
            model_name='salemodel',
            name='fk_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.clientmodel', verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='salemodel',
            name='fk_user_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='saledetailmodel',
            name='fk_sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.salemodel', verbose_name='Factura'),
        ),
        migrations.AddField(
            model_name='vouchertypemodel',
            name='fk_user_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='salemodel',
            name='fk_sale_voucher_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.vouchertypemodel', verbose_name='Tipo de Comprobante'),
        ),
        migrations.AddField(
            model_name='waytopaymodel',
            name='fk_user_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='salemodel',
            name='fk_way_to_pay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.waytopaymodel', verbose_name='Forma de Pago'),
        ),
    ]
