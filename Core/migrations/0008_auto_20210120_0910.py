# Generated by Django 3.1.5 on 2021-01-20 03:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0007_auto_20210120_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 20, 9, 10, 3, 887661)),
        ),
        migrations.AlterField(
            model_name='anwsers',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 20, 9, 10, 3, 880661)),
        ),
        migrations.AlterField(
            model_name='aptitude',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 20, 9, 10, 3, 889660)),
        ),
        migrations.AlterField(
            model_name='articles',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 20, 9, 10, 3, 878662)),
        ),
        migrations.AlterField(
            model_name='list',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 20, 9, 10, 3, 890683)),
        ),
    ]
