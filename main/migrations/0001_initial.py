# Generated by Django 2.0.6 on 2019-01-15 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id_imagen', models.AutoField(primary_key=True, serialize=False, verbose_name='id_imagen')),
                ('url', models.CharField(blank=True, max_length=256, null=True, verbose_name='Ruta de lamacenamiento estático')),
                ('imagen', models.ImageField(blank=True, help_text='Imagen adicional para Lugares o eventos', null=True, upload_to='generales')),
            ],
        ),
    ]
