# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-25 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=1000)),
                ('date', models.IntegerField(default=1)),
                ('month', models.CharField(max_length=200)),
                ('year', models.IntegerField(default=2018)),
                ('religion', models.CharField(default=None, max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('event_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=9000)),
                ('offers', models.CharField(max_length=200)),
            ],
        ),
    ]