# Generated by Django 4.2.7 on 2023-11-25 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=50, verbose_name='Nombres')),
                ('surnames', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('nationality', models.CharField(max_length=20, verbose_name='Nacionalidad')),
                ('age', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_date', models.DateField()),
                ('come_back_date', models.DateField(blank=True, null=True)),
                ('status', models.BooleanField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.book')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lector.reader')),
            ],
        ),
    ]
