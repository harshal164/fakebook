# Generated by Django 2.2 on 2019-11-05 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0009_auto_20191105_0600'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
