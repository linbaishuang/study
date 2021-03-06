# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 02:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrators',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('level', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('columnId', models.AutoField(primary_key=True, serialize=False)),
                ('parentColum', models.CharField(max_length=50)),
                ('sort', models.IntegerField()),
                ('level', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('is_use', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('departmentId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('imageId', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=100)),
                ('img', models.FileField(upload_to='picture')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('newsId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('create_date', models.DateField()),
                ('upload_date', models.DateField(null=True)),
                ('text', models.TextField()),
                ('writer', models.CharField(max_length=50)),
                ('is_stick', models.BooleanField(default=False)),
                ('columnId', models.ForeignKey(db_column='columnId', on_delete=django.db.models.deletion.CASCADE, to='admina.Column')),
                ('departmentId', models.ForeignKey(db_column='departmentId', on_delete=django.db.models.deletion.CASCADE, to='admina.Department')),
                ('imageId', models.ForeignKey(db_column='imageId', on_delete=django.db.models.deletion.CASCADE, to='admina.Image')),
            ],
        ),
        migrations.AddField(
            model_name='column',
            name='imageId',
            field=models.ForeignKey(db_column='imageId', on_delete=django.db.models.deletion.CASCADE, to='admina.Image'),
        ),
        migrations.AddField(
            model_name='administrators',
            name='departmentId',
            field=models.ForeignKey(db_column='departmentId', on_delete=django.db.models.deletion.CASCADE, to='admina.Department'),
        ),
    ]
