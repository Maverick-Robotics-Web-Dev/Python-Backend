# Generated by Django 5.0.2 on 2024-03-12 20:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashregisters', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashregistermodel',
            name='cash_register_created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 12, 15, 52, 58, 735798), verbose_name='Fecha de Creación'),
        ),
        migrations.AlterField(
            model_name='cashregistermovementsmodel',
            name='cash_register_movements_created_at',
            field=models.DateTimeField(default='marzo 12, 2024 - 15:52:58', verbose_name='Fecha de Creación'),
        ),
    ]