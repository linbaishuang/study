# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 04:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admina', '0003_administrators_is_use'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='parentColum',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
