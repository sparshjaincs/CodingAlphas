# Generated by Django 3.1.5 on 2021-01-26 02:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discuss', '0007_auto_20210126_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quora',
            name='dislike',
            field=models.ManyToManyField(null=True, related_name='Quora_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='quora',
            name='like',
            field=models.ManyToManyField(null=True, related_name='Quora_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
