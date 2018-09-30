# Generated by Django 2.1.1 on 2018-09-22 11:28

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicComment',
            fields=[
                ('nid', models.BigAutoField(primary_key=True, serialize=False)),
                ('content', ckeditor.fields.RichTextField(verbose_name='评论内容')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('parent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='c_comment', to='operation.TopicComment', verbose_name='子评论内容')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Topic', verbose_name='主题')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户主题评论',
                'verbose_name_plural': '用户主题评论',
                'ordering': ['-add_time'],
            },
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_id', models.IntegerField(default=0, verbose_name='收藏的主题ID')),
                ('add_time', models.DateTimeField(auto_now=True, verbose_name='收藏时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_fav', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户收藏',
                'verbose_name_plural': '用户收藏',
            },
        ),
    ]
