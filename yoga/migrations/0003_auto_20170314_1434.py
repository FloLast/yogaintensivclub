# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0002_auto_20170309_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.CharField(max_length=100)),
                ('durée', models.CharField(max_length=42)),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='categorie',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Categorie',
        ),
    ]
