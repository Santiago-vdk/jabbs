# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-02 15:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_auto_20160201_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='job_type',
        ),
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Job_Type'),
            preserve_default=False,
        ),
    ]
