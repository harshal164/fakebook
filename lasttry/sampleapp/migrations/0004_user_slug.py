# Generated by Django 2.2 on 2019-11-04 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0003_auto_20191104_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
