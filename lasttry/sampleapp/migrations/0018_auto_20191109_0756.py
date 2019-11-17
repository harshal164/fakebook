# Generated by Django 2.2 on 2019-11-09 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0017_auto_20191109_0658'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('postid', models.IntegerField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]