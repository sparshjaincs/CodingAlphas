# Generated by Django 3.1.5 on 2021-01-20 06:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0008_auto_20210120_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 20, 12, 15, 29, 402890)),
        ),
        migrations.AlterField(
            model_name='anwsers',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 20, 12, 15, 29, 397889)),
        ),
        migrations.AlterField(
            model_name='aptitude',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 20, 12, 15, 29, 404891)),
        ),
        migrations.AlterField(
            model_name='articles',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 20, 12, 15, 29, 395891)),
        ),
        migrations.AlterField(
            model_name='list',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 20, 12, 15, 29, 405889)),
        ),
    ]
