# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-04 14:27
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180203_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ReComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='data',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='images'),
        ),
        migrations.AddField(
            model_name='recomment',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
