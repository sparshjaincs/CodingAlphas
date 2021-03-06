# Generated by Django 3.1.5 on 2021-01-21 03:33

import ckeditor.fields
import datetime
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
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=1000, unique=True)),
                ('template', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Programming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, unique=True)),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('solution', ckeditor.fields.RichTextField(blank=True)),
                ('difficulty', models.CharField(choices=[('Easy', 'Easy'), ('Moderate', 'Moderate'), ('Hard', 'Hard')], default='Easy', max_length=100)),
                ('status', models.CharField(choices=[('Todo', 'Todo'), ('Solved', 'Solved'), ('Attempted', 'Attempted')], default='Todo', max_length=1000)),
                ('video', models.CharField(choices=[('Has solution', 'Has solution'), ('Has video solution', 'Has video solution')], default='Has solution', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Programming_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=1000, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Programming_Companies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=1000, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Untitled', max_length=1000)),
                ('question', models.ManyToManyField(blank=True, default=None, related_name='todo_question', to='Coding.Programming')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo_user', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cases', models.TextField()),
                ('sol_cases', models.TextField()),
                ('public_cases', models.TextField()),
                ('public_sol_cases', models.TextField()),
                ('instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testcase_ques', to='Coding.programming', to_field='title')),
            ],
        ),
        migrations.CreateModel(
            name='Templates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.TextField()),
                ('code', models.TextField(blank=True)),
                ('snippet', models.TextField(blank=True)),
                ('solution', models.TextField(blank=True)),
                ('instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temlate_ques', to='Coding.programming', to_field='title')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temp_lang_name', to='Coding.language', to_field='lang')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Wrong Anwser', 'Wrong Anwser'), ('Runtime Error', 'Runtime Error')], max_length=1000)),
                ('runtime', models.IntegerField(default=0)),
                ('time', models.DateField(default=datetime.datetime.now)),
                ('solution', models.TextField(default='')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission_lang', to='Coding.language', to_field='lang')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission_question', to='Coding.programming', to_field='title')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission_user', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, unique=True)),
                ('solution', ckeditor.fields.RichTextField(blank=True)),
                ('video', models.TextField(blank=True)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_sol', to='Coding.programming', to_field='title')),
            ],
        ),
        migrations.AddField(
            model_name='programming',
            name='category',
            field=models.ForeignKey(default='Arrays', on_delete=django.db.models.deletion.CASCADE, related_name='program_category', to='Coding.programming_category', to_field='category_name'),
        ),
        migrations.AddField(
            model_name='programming',
            name='company',
            field=models.ManyToManyField(blank=True, default=None, related_name='program_company', to='Coding.Programming_Companies'),
        ),
        migrations.AddField(
            model_name='programming',
            name='dislike',
            field=models.ManyToManyField(blank=True, default=None, related_name='program_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='programming',
            name='like',
            field=models.ManyToManyField(blank=True, default=None, related_name='program_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='programming',
            name='tags',
            field=models.ManyToManyField(blank=True, default=None, related_name='program_tags', to='Coding.Programming_Category'),
        ),
        migrations.CreateModel(
            name='Code_Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(blank=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='language_name', to='Coding.language', to_field='lang')),
                ('program', models.ForeignKey(default='Longest Palindromic Substring', on_delete=django.db.models.deletion.CASCADE, related_name='code_sol', to='Coding.programming', to_field='title')),
                ('solution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sol_Snippet', to='Coding.solution', to_field='title')),
            ],
        ),
    ]
