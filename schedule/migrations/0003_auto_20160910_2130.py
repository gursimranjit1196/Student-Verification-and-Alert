# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-10 16:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20160909_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timetable',
            old_name='_10AM',
            new_name='T10AM',
        ),
        migrations.RenameField(
            model_name='timetable',
            old_name='_11AM',
            new_name='T11AM',
        ),
        migrations.RenameField(
            model_name='timetable',
            old_name='_9AM',
            new_name='T9AM',
        ),
    ]