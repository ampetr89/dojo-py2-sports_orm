# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0004_auto_20170724_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='all_teams',
        ),
        migrations.AlterField(
            model_name='player',
            name='curr_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.Team'),
        ),
    ]
