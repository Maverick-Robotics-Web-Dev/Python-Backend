# Generated by Django 5.0.2 on 2024-02-26 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientmodel',
            name='client_status',
            field=models.BooleanField(default=False, verbose_name='Estado'),
        ),
    ]