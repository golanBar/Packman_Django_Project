# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0002_auto_20160104_1717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='avgScore',
            new_name='avg_score',
        ),
        migrations.RenameField(
            model_name='subscriber',
            old_name='bestScore',
            new_name='best_score',
        ),
        migrations.RenameField(
            model_name='subscriber',
            old_name='numGames',
            new_name='num_games',
        ),
    ]
