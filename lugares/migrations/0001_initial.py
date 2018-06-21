# Generated by Django 2.0.6 on 2018-06-20 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id_lugar', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=400)),
                ('capacidad', models.IntegerField()),
                ('direccion', models.CharField(max_length=150)),
            ],
        ),
    ]
