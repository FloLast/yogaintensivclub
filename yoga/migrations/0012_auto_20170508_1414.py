# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 12:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0011_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['date']},
        ),
        migrations.AlterModelOptions(
            name='sport',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['user__date__joined']},
        ),
    ]
