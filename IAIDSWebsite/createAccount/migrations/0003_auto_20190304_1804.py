# Generated by Django 2.2b1 on 2019-03-05 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createAccount', '0002_auto_20190304_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]