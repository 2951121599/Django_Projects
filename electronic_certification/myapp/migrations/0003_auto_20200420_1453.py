# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-04-20 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200420_1137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='image_name',
            new_name='img_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='img_img',
        ),
        migrations.AddField(
            model_name='user',
            name='img_url',
            field=models.ImageField(default='', upload_to='img', verbose_name='图片路径'),
        ),
    ]