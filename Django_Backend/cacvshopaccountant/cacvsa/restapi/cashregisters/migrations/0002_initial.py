# Generated by Django 5.0.2 on 2024-04-03 22:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0003_initial'),
        ('cashregisters', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cashregisterclosingmodel',
            name='fk_user_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='cashregistermodel',
            name='fk_user_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='cashregisterclosingmodel',
            name='fk_cash_register',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cashregisters.cashregistermodel', verbose_name='Caja'),
        ),
        migrations.AddField(
            model_name='cashregistermovementsmodel',
            name='fk_cash_register',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cashregisters.cashregistermodel', verbose_name='Caja'),
        ),
        migrations.AddField(
            model_name='cashregistermovementsmodel',
            name='fk_user_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='cashregistermovementsmodel',
            name='fk_way_to_pay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.waytopaymodel', verbose_name='Forma de Pago'),
        ),
        migrations.AddField(
            model_name='cashregisteropeningmodel',
            name='fk_cash_register',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cashregisters.cashregistermodel', verbose_name='Caja'),
        ),
        migrations.AddField(
            model_name='cashregisteropeningmodel',
            name='fk_user_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
