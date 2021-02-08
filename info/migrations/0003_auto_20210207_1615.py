# Generated by Django 3.1.6 on 2021-02-08 00:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_country'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.RenameField(
            model_name='info',
            old_name='message',
            new_name='kind',
        ),
        migrations.AddField(
            model_name='info',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 2, 7, 16, 15, 47, 977996)),
        ),
        migrations.AlterField(
            model_name='info',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]