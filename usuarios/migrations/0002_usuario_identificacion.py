# Generated by Django 2.0.6 on 2018-06-21 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='identificacion',
            field=models.CharField(default=1, max_length=20),
        ),
    ]
