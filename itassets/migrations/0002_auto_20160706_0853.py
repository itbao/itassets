# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itassets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpus',
            name='cpu',
            field=models.CharField(max_length=20),
        ),
    ]