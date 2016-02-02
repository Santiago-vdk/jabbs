# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_auto_20160201_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Type',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=24, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_type',
        ),
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.ManyToManyField(to='jobs.Job_Type'),
        ),
    ]
