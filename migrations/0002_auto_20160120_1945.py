# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_squashed_0009_auto_20160117_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='emp_id',
            field=models.ForeignKey(db_column='emp_id', default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.Employee'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='qu_id',
            field=models.ForeignKey(db_column='qu_id', default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.Question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='uid',
            field=models.ForeignKey(db_column='uid', default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.People'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qu_id',
            field=models.AutoField(db_column='qu_id', primary_key=True, serialize=False),
        ),
    ]
