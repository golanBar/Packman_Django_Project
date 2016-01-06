# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
        ('subscribers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='avgScore',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='bestScore',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='numGames',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='team',
            field=models.ForeignKey(null=True, to='teams.Team'),
        ),
    ]
