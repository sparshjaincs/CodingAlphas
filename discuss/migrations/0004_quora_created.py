# Generated by Django 3.1.5 on 2021-01-25 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discuss', '0003_auto_20210125_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='quora',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
