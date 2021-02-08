# Generated by Django 3.1.6 on 2021-02-08 01:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_auto_20210207_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Physicians',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(default='', max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='info',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 2, 7, 17, 8, 46, 260701)),
        ),
    ]
