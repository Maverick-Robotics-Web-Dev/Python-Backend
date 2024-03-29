# Generated by Django 5.0.1 on 2024-01-23 03:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('suppliers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='incomemodel',
            name='fk_user_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='incomedetailmodel',
            name='fk_income',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.incomemodel', verbose_name='Ingreso'),
        ),
        migrations.AddField(
            model_name='suppliermodel',
            name='fk_user_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='incomemodel',
            name='fk_supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.suppliermodel', verbose_name='Proveedor'),
        ),
    ]
