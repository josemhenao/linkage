# Generated by Django 2.0.6 on 2018-07-13 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rol',
            name='permisos',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='rol',
        ),
        migrations.DeleteModel(
            name='Permiso',
        ),
        migrations.DeleteModel(
            name='Rol',
        ),
    ]
