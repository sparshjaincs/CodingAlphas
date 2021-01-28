# Generated by Django 3.1.5 on 2021-01-10 16:07

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
            name='Anwsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(default=datetime.datetime(2021, 1, 10, 21, 37, 22, 66703))),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('description', models.TextField(blank=True, default='')),
                ('explanation', ckeditor.fields.RichTextField(null=True)),
            ],
            options={
                'ordering': ('-date', '-time'),
            },
        ),
        migrations.CreateModel(
            name='Aptitude',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', ckeditor.fields.RichTextField(unique=True)),
                ('A', models.TextField(blank=True, default='')),
                ('B', models.TextField(blank=True, default='')),
                ('C', models.TextField(blank=True, default='')),
                ('D', models.TextField(blank=True, default='')),
                ('E', models.TextField(blank=True, default='', null=True)),
                ('correct', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=10)),
                ('difficulty', models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], max_length=10)),
                ('time', models.TimeField(default=datetime.datetime(2021, 1, 10, 21, 37, 22, 72711))),
                ('date_Publish', models.DateField(default=datetime.datetime.now)),
                ('exam_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('explanation', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField(default=' ', unique=True)),
                ('project_name', models.CharField(max_length=100)),
                ('author', models.CharField(blank=True, max_length=50)),
                ('date_Publish', models.DateField(default=datetime.datetime.now)),
                ('date_updated', models.DateField(default=datetime.datetime.now)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='users/images')),
                ('video', models.FileField(blank=True, null=True, upload_to='users/video', verbose_name='Video')),
                ('image2', models.CharField(blank=True, max_length=1000, null=True)),
                ('content', ckeditor.fields.RichTextField(null=True)),
                ('link', models.TextField(blank=True, default='')),
                ('description', models.TextField(blank=True, default='')),
                ('time', models.TimeField(default=datetime.datetime(2021, 1, 10, 21, 37, 22, 65703))),
                ('tags', models.CharField(default='', help_text='Add comma( ,) seperated tags!!', max_length=300, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
                ('method', models.CharField(choices=[('blog', 'blog'), ('design', 'design'), ('editor', 'editor'), ('learn', 'learn')], default='blog', max_length=10)),
                ('template', models.CharField(blank=True, max_length=1000, null=True)),
                ('quora', models.CharField(blank=True, max_length=1000, null=True)),
                ('medium', models.CharField(blank=True, max_length=1000, null=True)),
                ('facebook', models.CharField(blank=True, max_length=1000, null=True)),
                ('instagram', models.CharField(blank=True, max_length=1000, null=True)),
                ('twitter', models.CharField(blank=True, max_length=1000, null=True)),
                ('other', models.CharField(blank=True, max_length=1000, null=True)),
                ('question_field', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('date_Publish', 'time'),
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('All', 'All'), ('Quants', 'Quants'), ('Verbal', 'Verbal'), ('Logical', 'Logical')], default='All', max_length=1000)),
                ('category_name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='', max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, default='')),
                ('heading', models.TextField(blank=True, default='')),
                ('link', models.TextField(blank=True, default='')),
                ('time', models.TimeField(default=datetime.datetime(2021, 1, 10, 21, 37, 22, 73705))),
                ('date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(default='', max_length=40, unique=True)),
                ('choice', models.ForeignKey(default='All', on_delete=django.db.models.deletion.CASCADE, related_name='catview', to='Core.categories', to_field='category_name')),
            ],
        ),
        migrations.CreateModel(
            name='titleview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_addr', models.CharField(blank=True, max_length=300, null=True)),
                ('view', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titleview', to='Core.articles')),
            ],
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side_data', models.TextField(null=True)),
                ('pattern', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('syll', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('experience', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='Core.company', to_field='company_name')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=50)),
                ('last_name', models.CharField(blank=True, default='', max_length=50)),
                ('email', models.EmailField(blank=True, default='', max_length=50)),
                ('phone_number', models.CharField(blank=True, default='', max_length=13)),
                ('avatar', models.ImageField(default='users/images/default.jpg', upload_to='users/images')),
                ('headline', models.CharField(blank=True, default='', max_length=1000)),
                ('bio', models.TextField(blank=True, default='')),
                ('address', models.CharField(blank=True, default='', max_length=50)),
                ('city', models.CharField(blank=True, default='', max_length=50)),
                ('state', models.CharField(blank=True, default='', max_length=50)),
                ('country', models.CharField(blank=True, default='', max_length=50)),
                ('date_of_birth', models.CharField(blank=True, default='', max_length=13)),
                ('signup_confirmation', models.BooleanField(default=False)),
                ('instagram', models.CharField(blank=True, max_length=1000, null=True)),
                ('facebook', models.CharField(blank=True, max_length=1000, null=True)),
                ('twitter', models.CharField(blank=True, max_length=1000, null=True)),
                ('college', models.CharField(blank=True, default='', max_length=1000)),
                ('medium', models.CharField(blank=True, max_length=1000, null=True)),
                ('quora', models.CharField(blank=True, max_length=1000, null=True)),
                ('other', models.CharField(blank=True, max_length=1000, null=True)),
                ('favourities', models.ManyToManyField(blank=True, related_name='articles_titles', to='Core.Articles')),
                ('follow', models.ManyToManyField(blank=True, default=None, related_name='follow_title', to=settings.AUTH_USER_MODEL)),
                ('following', models.ManyToManyField(blank=True, default=None, related_name='following_title', to=settings.AUTH_USER_MODEL)),
                ('mute', models.ManyToManyField(blank=True, default=None, related_name='mute_title', to=settings.AUTH_USER_MODEL)),
                ('subscribe', models.ManyToManyField(blank=True, default=None, related_name='subscribe_title', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_count', models.IntegerField(default=0)),
                ('activity_profile_count', models.IntegerField(default=0)),
                ('follow_count', models.IntegerField(default=0)),
                ('following_count', models.IntegerField(default=0)),
                ('user_name4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_name4_notification', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='my_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Core.my_comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_comments', to='Core.articles')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, unique=True)),
                ('status', models.CharField(choices=[('All', 'All'), ('Free', 'Free'), ('Paid', 'Paid')], default='All', max_length=1000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Module_Category', to='Core.categories', to_field='category_name')),
                ('company', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Module_Companies', to='Core.company', to_field='company_name')),
                ('question', models.ManyToManyField(related_name='Module_Question', to='Core.Aptitude')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Module_Topic', to='Core.topic', to_field='topic_name')),
            ],
        ),
        migrations.CreateModel(
            name='Discussion_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(blank=True, max_length=100000)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Core.discussion_comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussion', to='Core.anwsers')),
                ('user_discussion', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_discussion_1', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='articles',
            name='category',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, related_name='category', to='Core.categories', to_field='category_name'),
        ),
        migrations.AddField(
            model_name='articles',
            name='disliked',
            field=models.ManyToManyField(blank=True, default=None, related_name='dislikes_title', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='articles',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, related_name='likes_title', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='articles',
            name='user_name2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_username_2', to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
        migrations.AddField(
            model_name='aptitude',
            name='category',
            field=models.ForeignKey(default='Quants', on_delete=django.db.models.deletion.CASCADE, related_name='categoryname1', to='Core.categories', to_field='category_name'),
        ),
        migrations.AddField(
            model_name='aptitude',
            name='company',
            field=models.ForeignKey(default='Accenture', on_delete=django.db.models.deletion.CASCADE, related_name='companyname', to='Core.company', to_field='company_name'),
        ),
        migrations.AddField(
            model_name='aptitude',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topicname', to='Core.topic', to_field='topic_name'),
        ),
        migrations.AddField(
            model_name='anwsers',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_question_4', to='Core.articles', to_field='title'),
        ),
        migrations.AddField(
            model_name='anwsers',
            name='user_anwser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_anwser_1', to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
        migrations.CreateModel(
            name='activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_activity', models.CharField(blank=True, max_length=200)),
                ('activity_icon', models.CharField(blank=True, max_length=200)),
                ('category', models.CharField(choices=[('User', 'User')], default='User', max_length=1000)),
                ('activity_time', models.TimeField(default=datetime.datetime(2021, 1, 10, 21, 37, 22, 70703))),
                ('color', models.CharField(default='text-info', max_length=100)),
                ('date_activity', models.DateField(default=datetime.datetime.now)),
                ('activity_count', models.IntegerField(default=0, null=True)),
                ('user_name3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_username_3', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='Job_Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1000)),
                ('location', models.CharField(blank=True, max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_Jobs', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'unique_together': {('title', 'location')},
            },
        ),
    ]
