# Generated by Django 3.1.5 on 2021-01-25 07:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0019_auto_20210125_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 25, 12, 42, 20, 607394)),
        ),
        migrations.AlterField(
            model_name='anwsers',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 25, 12, 42, 20, 599394)),
        ),
        migrations.AlterField(
            model_name='aptitude',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 25, 12, 42, 20, 615392)),
        ),
        migrations.AlterField(
            model_name='articles',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 25, 12, 42, 20, 599394)),
        ),
        migrations.AlterField(
            model_name='list',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 25, 12, 42, 20, 615392)),
        ),
    ]
