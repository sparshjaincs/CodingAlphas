# Generated by Django 3.1.5 on 2021-01-21 03:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0010_auto_20210120_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 21, 9, 3, 42, 349061)),
        ),
        migrations.AlterField(
            model_name='anwsers',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 21, 9, 3, 42, 348095)),
        ),
        migrations.AlterField(
            model_name='aptitude',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 21, 9, 3, 42, 357690)),
        ),
        migrations.AlterField(
            model_name='articles',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 21, 9, 3, 42, 338929)),
        ),
        migrations.AlterField(
            model_name='list',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 21, 9, 3, 42, 358318)),
        ),
    ]