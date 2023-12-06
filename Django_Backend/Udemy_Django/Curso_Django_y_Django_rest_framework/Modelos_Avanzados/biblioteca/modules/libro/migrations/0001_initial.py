# Generated by Django 4.2.7 on 2023-11-25 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titutlo')),
                ('release_date', models.DateField(verbose_name='Fecha de Lanzamiento')),
                ('front_page', models.ImageField(upload_to='portada', verbose_name='Portada')),
                ('visits', models.PositiveIntegerField()),
                ('authors', models.ManyToManyField(to='autor.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.category')),
            ],
        ),
    ]