# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-12 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='poem_id',
            field=models.IntegerField(default=0),
        ),
    ]
