# Generated by Django 2.1.7 on 2019-04-17 01:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgAdminPanel', '0005_auto_20190416_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='endtime',
            field=models.TimeField(default=datetime.time(17, 6, 1, 860045)),
        ),
        migrations.AlterField(
            model_name='event',
            name='starttime',
            field=models.TimeField(default=datetime.time(17, 6, 1, 859993)),
        ),
        migrations.AlterField(
            model_name='job',
            name='endtime',
            field=models.TimeField(default=datetime.time(17, 6, 1, 866721)),
        ),
        migrations.AlterField(
            model_name='job',
            name='starttime',
            field=models.TimeField(default=datetime.time(17, 6, 1, 866678)),
        ),
    ]
