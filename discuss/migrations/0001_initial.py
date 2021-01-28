# Generated by Django 3.1.5 on 2021-01-24 03:54

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anwsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anwser', ckeditor_uploader.fields.RichTextUploadingField()),
                ('dislike', models.ManyToManyField(related_name='anwser_dislike', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Quora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor_uploader.fields.RichTextUploadingField(unique=True)),
                ('dislike', models.ManyToManyField(related_name='Quora_dislikes', to=settings.AUTH_USER_MODEL)),
                ('like', models.ManyToManyField(related_name='Quora_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discuss.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Anwser_comment', to='discuss.anwsers')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Quora_Comment', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='anwsers',
            name='instance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Quora_anwsers', to='discuss.quora', to_field='title'),
        ),
        migrations.AddField(
            model_name='anwsers',
            name='like',
            field=models.ManyToManyField(related_name='anwser_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
