# Generated by Django 2.0.6 on 2019-01-22 04:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(help_text='Nombre la categoría', max_length=60, unique=True)),
                ('descripcion', models.CharField(help_text='Descripción de la categoría', max_length=400)),
            ],
            options={
                'verbose_name': 'Categoria',
                'ordering': ['id_categoria'],
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id_ciudad', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('ciudad', models.CharField(default='', help_text='Nombre de la ciudad', max_length=255)),
                ('estado', models.CharField(help_text='Estado actual de la Ciudad, 0:inactivo, 1:activo', max_length=1)),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
                'ordering': ['ciudad', 'departamento', 'estado'],
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id_departamento', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('departamento', models.CharField(default='', max_length=255)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
                'ordering': ['departamento', 'id_departamento'],
            },
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id_lugar', models.AutoField(primary_key=True, serialize=False, verbose_name='Id_lugar')),
                ('slug', models.SlugField(unique=True)),
                ('nombre', models.CharField(help_text='Nombre del Lugar', max_length=60, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, help_text='Descripción del Lugar', max_length=400, null=True)),
                ('capacidad', models.IntegerField(help_text='Número de personas que caben en el Lugar')),
                ('direccion', models.CharField(blank=True, help_text='Dirección del Lugar', max_length=150, null=True)),
                ('img_ppal', models.ImageField(blank=True, default='lugares/img/lugar/default_lugar_ppal.png', help_text='Imagen principal del Lugar', null=True, upload_to='lugares/img/lugar')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('admin', models.ForeignKey(blank=True, help_text='Usuarios de la plataforma que administra este Lugar', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ciudad', models.ForeignKey(help_text='Ciudad donde se ubica el establecimiento', on_delete=django.db.models.deletion.CASCADE, to='lugares.Ciudad')),
                ('imagenes', models.ManyToManyField(blank=True, null=True, to='main.Imagen', verbose_name='Lista de imagenes')),
            ],
            options={
                'verbose_name': 'Lugar',
                'verbose_name_plural': 'Lugares',
                'ordering': ['id_lugar', 'nombre'],
            },
        ),
        migrations.AddField(
            model_name='ciudad',
            name='departamento',
            field=models.ForeignKey(help_text='FK al departamento al que se pertenece', on_delete=django.db.models.deletion.CASCADE, to='lugares.Departamento'),
        ),
    ]
