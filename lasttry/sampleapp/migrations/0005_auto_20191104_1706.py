# Generated by Django 2.2 on 2019-11-04 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0004_user_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(default='this-is-my-slug'),
        ),
    ]
