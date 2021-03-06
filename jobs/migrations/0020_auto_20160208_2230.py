# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 04:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0019_school_initials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Job_Type'),
        ),
    ]
