# Generated by Django 3.1.6 on 2021-02-08 00:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20210207_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='doctor',
            field=models.CharField(default='None', max_length=300),
        ),
        migrations.AlterField(
            model_name='info',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 2, 7, 16, 17, 52, 35536)),
        ),
    ]
