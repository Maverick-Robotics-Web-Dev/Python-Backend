# Generated by Django 5.0.1 on 2024-02-08 17:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('suppliers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='brandmodel',
            name='fk_user_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='fk_user_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='fk_brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.brandmodel', verbose_name='Marca'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='fk_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categorymodel', verbose_name='Categoria'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='fk_supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.suppliermodel', verbose_name='Proveedor'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='fk_user_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
