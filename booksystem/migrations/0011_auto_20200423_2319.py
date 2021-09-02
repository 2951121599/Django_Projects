# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-04-23 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksystem', '0010_auto_20200423_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='sex',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=50, verbose_name='性别'),
        ),
    ]
