# Generated by Django 5.0.2 on 2024-03-12 18:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0001_initial'),
        ('clients', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditnotedetailmodel',
            name='fk_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productmodel', verbose_name='Producto'),
        ),
        migrations.AddField(
            model_name='creditnotemodel',
            name='fk_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.clientmodel', verbose_name='Cliente'),
        ),
    ]
