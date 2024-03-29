# Generated by Django 5.0.1 on 2024-01-23 03:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('clients', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLevelModel',
            fields=[
                ('user_level_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('user_level_name', models.CharField(max_length=256, verbose_name='Nombre del Nivel')),
                ('user_level_status', models.CharField(max_length=50, verbose_name='Estado')),
                ('user_level_status_description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Descripción')),
                ('user_level_create_at', models.DateTimeField(verbose_name='Fecha de Creación')),
                ('user_level_update_at', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Actualización')),
            ],
            options={
                'verbose_name': 'NIVEL DE USUARIO',
                'verbose_name_plural': 'NIVELES DE USUARIO',
                'db_table': 'APIS_USER_LEVEL',
            },
        ),
        migrations.CreateModel(
            name='UserClientModel',
            fields=[
                ('user_client_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('user_client_user_name', models.CharField(max_length=256, verbose_name='Nombre de Usuario')),
                ('user_client_password', models.CharField(max_length=16, verbose_name='Contraseña')),
                ('user_client_login', models.BooleanField(verbose_name='Logueado')),
                ('user_client_status', models.CharField(max_length=50, verbose_name='Estado')),
                ('user_client_status_description', models.CharField(default='Ninguna', max_length=256, verbose_name='Descripción')),
                ('user_client_create_at', models.DateTimeField(verbose_name='Fecha de Creación')),
                ('user_client_update_at', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Actualización')),
                ('fk_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.clientmodel', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'USUARIO DEL CLIENTE',
                'verbose_name_plural': 'USUARIOS DEL CLIENTE',
                'db_table': 'APIS_USER_CLIENT',
            },
        ),
        migrations.CreateModel(
            name='UserEmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_employee_user_name', models.CharField(max_length=20, unique=True, verbose_name='Nombre de Usuario')),
                ('user_employee_login', models.BooleanField(blank=True, null=True, verbose_name='Logueado')),
                ('user_employee_status', models.CharField(blank=True, max_length=50, null=True, verbose_name='Estado')),
                ('user_employee_status_description', models.CharField(default='Ninguna', max_length=256, verbose_name='Descripción')),
                ('user_employee_create_at', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Creación')),
                ('user_employee_update_at', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Actualización')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('fk_employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.employeemodel', verbose_name='Empeado')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('fk_user_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userlevelmodel', verbose_name='Nivel')),
            ],
            options={
                'verbose_name': 'USURIO DE EMPLEADO',
                'verbose_name_plural': 'USUARIOS DE EMPLEADO',
                'db_table': 'APIS_USER_EMPLOYEE',
            },
        ),
    ]
