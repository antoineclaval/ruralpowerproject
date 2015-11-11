# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coopInfo', '0005_auto_20150213_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperative',
            name='acronym',
            field=models.CharField(max_length=6, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='annualMeeting',
            field=models.CharField(max_length=500, verbose_name=b'info about annual meeting', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='bylaws',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='countiesServed',
            field=models.CharField(max_length=500, verbose_name=b'counties served', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='email',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='mailAddress',
            field=models.CharField(max_length=50, verbose_name=b'mail address', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='montlyMeeting',
            field=models.CharField(max_length=500, verbose_name=b'info about montly meeting', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='nextElectionTerms',
            field=models.CharField(max_length=50, verbose_name=b'next election', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='phone',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='servingTime',
            field=models.CharField(max_length=50, verbose_name=b'serving time', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='streetAddress',
            field=models.CharField(max_length=150, verbose_name=b'street address', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='website',
            field=models.CharField(unique=True, max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='distric',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='ethnicity',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='inBoardSince',
            field=models.DateTimeField(null=True, verbose_name=b'in board since', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
    ]
