# Generated by Django 2.0.6 on 2018-06-25 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evento',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['id_ticket']},
        ),
    ]