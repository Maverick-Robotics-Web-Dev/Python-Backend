# Generated by Django 5.0.2 on 2024-04-08 21:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='clientcheckmodel',
            name='fk_user_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='clientmodel',
            name='fk_user_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='clientcheckmodel',
            name='fk_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.clientmodel', verbose_name='Cliente'),
        ),
    ]
