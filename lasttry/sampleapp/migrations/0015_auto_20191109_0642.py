# Generated by Django 2.2 on 2019-11-09 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0014_filemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
