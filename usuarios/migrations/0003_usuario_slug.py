# Generated by Django 2.0.6 on 2018-06-27 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20180626_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='slug',
            field=models.SlugField(default='josem.henao1', max_length=40),
            preserve_default=False,
        ),
    ]