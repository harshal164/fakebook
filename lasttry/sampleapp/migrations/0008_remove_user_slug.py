# Generated by Django 2.2 on 2019-11-05 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0007_auto_20191104_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='slug',
        ),
    ]
