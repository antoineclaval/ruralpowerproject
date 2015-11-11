# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cooperative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('acronym', models.CharField(max_length=6)),
                ('streetAddress', models.CharField(max_length=50)),
                ('website', models.CharField(unique=True, max_length=255)),
                ('mailAddress', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('countiesServed', models.CharField(max_length=500)),
                ('consumers', models.IntegerField(default=0)),
                ('montlyMeeting', models.CharField(max_length=20)),
                ('annualMeeting', models.CharField(max_length=20)),
                ('numberOfEmployees', models.IntegerField(default=0)),
                ('milesOfLines', models.IntegerField(default=0)),
                ('nextElectionTerms', models.CharField(max_length=50)),
                ('servingTime', models.CharField(max_length=50)),
                ('bylaws', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('ethnicity', models.CharField(max_length=10)),
                ('distric', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=20)),
                ('inBoardSince', models.DateTimeField()),
                ('coopId', models.ForeignKey(to='coopInfo.Cooperative')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cooperative',
            name='stateId',
            field=models.ForeignKey(to='coopInfo.State'),
            preserve_default=True,
        ),
    ]
