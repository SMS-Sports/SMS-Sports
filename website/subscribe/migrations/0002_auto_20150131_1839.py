# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='euteam',
            old_name='soccer_region',
            new_name='team',
        ),
        migrations.RenameField(
            model_name='nateam',
            old_name='soccer_region',
            new_name='team',
        ),
        migrations.RemoveField(
            model_name='region',
            name='soccer_region',
        ),
        migrations.AddField(
            model_name='region',
            name='Region',
            field=models.CharField(default='USA', max_length=3, choices=[('USA', 'USA'), ('EU', 'Europe')]),
            preserve_default=True,
        ),
    ]
