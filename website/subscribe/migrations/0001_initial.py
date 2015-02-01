# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EUTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('soccer_region', models.CharField(max_length=4, default='MAD', choices=[('MAD', 'Real Madrid'), ('BAR', 'Barcelona'), ('ATL', 'Atletico Madrid'), ('MCY', 'Manchester City'), ('CHE', 'Cheslea'), ('ARS', 'Arsenal'), ('LIV', 'Liverpool'), ('MNU', 'Manchester United'), ('TOT', 'Tottenham Hotspur'), ('PSG', 'Paris St. Germain'), ('OL', 'Lyon'), ('MIL', 'AC Milan'), ('JUV', 'Juventus'), ('INT', 'Inter Milan'), ('NAP', 'Napoli'), ('ROMA', 'Roma'), ('BMU', 'Bayern Munich'), ('BOR', 'Borussia Dortmund')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NATeam',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('soccer_region', models.CharField(max_length=4, default='SEA', choices=[('SEA', 'Seattle Sounders'), ('NYR', 'New York Redbulls'), ('LAG', 'LA Galaxy'), ('TFC', 'Toronto FC'), ('REV', 'New England Revolution'), ('CHS', 'Chivas USA'), ('NYC', 'NYC FC'), ('POR', 'Portland Timbers'), ('VAN', 'Vancouver Whitecaps'), ('PHI', 'Philadelphia Union'), ('RSL', 'Real Salt Lake'), ('DCU', 'DC United'), ('COL', 'Columbus Crew'), ('SJE', 'San Jose Earthquaks'), ('ORL', 'Orlando City FC'), ('HOU', 'Houston Dynamo'), ('DAL', 'FC Dallas'), ('MTL', 'Montreal Impact'), ('CHI', 'Chicago Fire'), ('CDO', 'Colorado Rapids'), ('ATL', 'Atanta')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('soccer_region', models.CharField(max_length=2, default='USA', choices=[('USA', 'USA'), ('EU', 'Europe')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='nateam',
            name='region',
            field=models.ForeignKey(to='subscribe.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='euteam',
            name='region',
            field=models.ForeignKey(to='subscribe.Region'),
            preserve_default=True,
        ),
    ]
