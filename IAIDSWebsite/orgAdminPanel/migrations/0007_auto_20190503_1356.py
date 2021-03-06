# Generated by Django 2.1.7 on 2019-05-03 21:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgAdminPanel', '0006_auto_20190416_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='page',
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(default='What is this event about?'),
        ),
        migrations.AlterField(
            model_name='event',
            name='endtime',
            field=models.TimeField(default=datetime.time(13, 56, 9, 37621)),
        ),
        migrations.AlterField(
            model_name='event',
            name='starttime',
            field=models.TimeField(default=datetime.time(13, 56, 9, 37587)),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(default='What is this job about?'),
        ),
        migrations.AlterField(
            model_name='job',
            name='endtime',
            field=models.TimeField(default=datetime.time(13, 56, 9, 41923)),
        ),
        migrations.AlterField(
            model_name='job',
            name='starttime',
            field=models.TimeField(default=datetime.time(13, 56, 9, 41894)),
        ),
        migrations.AlterField(
            model_name='organization',
            name='description',
            field=models.TextField(default='What is your organization about?'),
        ),
    ]
