# Generated by Django 2.0.6 on 2018-06-20 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='id_lugar',
            field=models.IntegerField(auto_created=True, blank=True, primary_key=True, serialize=False, unique=True),
        ),
    ]