# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coopInfo', '0004_auto_20150203_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperative',
            name='annualMeeting',
            field=models.CharField(max_length=500, verbose_name=b'info about annual meeting'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='consumers',
            field=models.IntegerField(default=0, null=True, verbose_name=b'number of consumers'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='countiesServed',
            field=models.CharField(max_length=500, verbose_name=b'counties served'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='mailAddress',
            field=models.CharField(max_length=50, verbose_name=b'mail address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='milesOfLines',
            field=models.IntegerField(default=0, null=True, verbose_name=b'miles of electric lines'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='montlyMeeting',
            field=models.CharField(max_length=500, verbose_name=b'info about montly meeting'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='nextElectionTerms',
            field=models.CharField(max_length=50, verbose_name=b'next election'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='numberOfEmployees',
            field=models.IntegerField(default=0, null=True, verbose_name=b'number of employees'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='servingTime',
            field=models.CharField(max_length=50, verbose_name=b'serving time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='streetAddress',
            field=models.CharField(max_length=150, verbose_name=b'street address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='inBoardSince',
            field=models.DateTimeField(null=True, verbose_name=b'in board since'),
            preserve_default=True,
        ),
    ]
