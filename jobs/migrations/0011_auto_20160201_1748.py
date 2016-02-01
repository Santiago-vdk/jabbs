# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_auto_20160127_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='school',
            field=models.ManyToManyField(to='jobs.School'),
        ),
    ]
