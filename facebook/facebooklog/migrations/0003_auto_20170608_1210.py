# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebooklog', '0002_auto_20170608_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=50)),
                ('paswd', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='tbl_user',
        ),
    ]
