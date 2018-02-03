# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-03 00:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180202_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='upload_time',
        ),
        migrations.AddField(
            model_name='post',
            name='data',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='file_name',
            field=models.CharField(max_length=50),
        ),
    ]