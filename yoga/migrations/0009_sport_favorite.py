# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0008_sport'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]