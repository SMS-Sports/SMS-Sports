# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0002_auto_20150131_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='euteam',
            name='region',
        ),
        migrations.RemoveField(
            model_name='euteam',
            name='team',
        ),
        migrations.RemoveField(
            model_name='nateam',
            name='region',
        ),
        migrations.RemoveField(
            model_name='nateam',
            name='team',
        ),
        migrations.RemoveField(
            model_name='region',
            name='Region',
        ),
        migrations.AddField(
            model_name='euteam',
            name='name',
            field=models.CharField(default='Europe', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nateam',
            name='name',
            field=models.CharField(default='Real Madrid', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='region',
            name='name',
            field=models.CharField(default='Europe', max_length=30),
            preserve_default=False,
        ),
    ]
