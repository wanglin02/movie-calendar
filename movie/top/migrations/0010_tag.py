# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-11 07:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('passport', '0001_initial'),
        ('top', '0009_movie_ratings_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_going', models.BooleanField(default=False)),
                ('is_done', models.BooleanField(default=False)),
                ('operate_time', models.DateTimeField(auto_now=True, verbose_name='操作时间')),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='top.Movie')),
                ('users', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='passport.WeixinUsers')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]