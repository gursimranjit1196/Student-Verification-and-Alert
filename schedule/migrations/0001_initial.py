# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-09 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.CharField(blank=True, max_length=120, null=True)),
                ('Monday', models.CharField(blank=True, max_length=120, null=True)),
                ('Tuesday', models.CharField(blank=True, max_length=120, null=True)),
                ('Wednesday', models.CharField(blank=True, max_length=120, null=True)),
                ('Thursday', models.CharField(blank=True, max_length=120, null=True)),
                ('Friday', models.CharField(blank=True, max_length=120, null=True)),
                ('Saturday', models.CharField(blank=True, max_length=120, null=True)),
                ('Sunday', models.CharField(blank=True, max_length=120, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
